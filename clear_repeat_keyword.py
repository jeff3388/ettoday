# 去除重複字串
import numpy as np

with open('ETtoday_keyword.txt','r',encoding='utf-8') as txtfile:
    keywords_ls = txtfile.read().split(',')

num_ls = np.unique(keywords_ls) # num_ls 排序不變
content = ",".join(num_ls)

with open('ETtoday_keyword.txt','w',encoding='utf-8') as txtfile:
    txtfile.write(content)