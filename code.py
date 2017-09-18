#!/usr/bin/env python3
#-*-coding:utf-8 -*-
#author by ForEver
from bs4 import BeautifulSoup
import requests 
import urllib
from urllib import request
import os

payload = {}
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '     
                    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
     'Referer': 'http://www.xiami.com',
      'Connection': 'keep-alive'
  }
r = requests.get("http://www.xiami.com/", params=payload,headers=headers)
soup=BeautifulSoup(r.text,"lxml")
print (soup)#格式化输出
print("###########################")
print(soup.find_all('div', class_='image'))
img_src=[]
i=0
for myimg in soup.find_all('div', class_='image'):
	 #pic_name=str(i)+".jpg"
     img_src = myimg.find('img').get('src')
     pic_name=str(i)+".jpg"
     request.urlretrieve(img_src, pic_name)
     i+=1
     print(img_src)

print("@@@@@@@@@@@@@@")
