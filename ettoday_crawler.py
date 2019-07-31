# -*- coding:utf-8 -*- 

# ETtoday 暴力撈關鍵字

from bs4 import BeautifulSoup
import requests as res
import random
import time
import re

t = random.randint(1, 2)

headers = {
            'content-type': 'text/html; charset=utf-8', # attention code
            'content-encoding': 'gzip',
            'server': 'nginx',
            'status': '200',
            'vary': 'Accept-Encoding',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'accept': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://www.ettoday.net/events/passback/scupio/ad_300x600_2_FL-HB-2.htm',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }


house_tag_ls = [] # 房地產新聞 → 關鍵字
s = res.Session()
try:
    for i in range(900000,1000000): # 1430000
        try:
            house_url = 'https://house.ettoday.net/news/' + str(i)
            html = s.get(house_url,headers=headers,timeout=15).content
            soup = BeautifulSoup(html, 'html.parser')
            tag_class = soup.find_all("p", attrs={"class": "tag"})
            time.sleep(t)

            for tag in tag_class:
                tag = tag.text
                key_str = re.sub(r'[關鍵字： 雲論]', '', tag)
                key_ls = key_str.split("\n")
                for k in key_ls:
                    if k not in ['']:
                        if '﹑' in k:
                            k = k.split("﹑")
                            for v in k:
                                house_tag_ls += [v]
                        elif '、' in t:
                            k = k.split("、")
                            for v in t:
                                house_tag_ls += [v]
                        else:
                            house_tag_ls += [k]

            print("次數: " + str(i))
            print("關鍵字數量: " + str(len(house_tag_ls)))
        except Exception as e:
            print(e)
            time.sleep(10)
except:
    pass


house_tag_ls = list(set(house_tag_ls)) # 去除重複關鍵字


#### 重造關鍵字權重 ####
# tk_ls = []

# for total_keyword in house_tag_ls:
    
#     if len(total_keyword) == 1:
#         tk = total_keyword + ' 1\n'
#         tk_ls += [tk]
        
#     elif len(total_keyword) == 2:
#         tk = total_keyword + ' 3\n'
#         tk_ls += [tk]
        
#     elif len(total_keyword) == 3:
#         tk = total_keyword + ' 5\n'
#         tk_ls += [tk]
        
#     else:
#         tk = total_keyword + ' 10\n'
#         tk_ls += [tk]

content = ",".join(house_tag_ls)                
                    
with open("./ETtoday_keyword.txt","a",encoding="utf-8",errors="ingnor") as keywords:
    keywords.write("," + content)