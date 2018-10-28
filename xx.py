#!/usr/bin/env python3
#-*-coding:utf-8 -*-
#author by ForEver
#-*-coding:utf8-*-

from bs4 import BeautifulSoup
import requests
import os

cookie = {"Cookie": "_T_WM=xxxx; ALF=xxxxxx; SCF=xxxx; SUB=xxx; SUBP=x; SUHB=x; M_WEIBOCN_PARAMS=xx"}
url = 'https://weibo.cn/xxxxxxxxxx/profile?filter=1&page=1'
r = requests.get(url,cookies = cookie)
print(r.url)

soup=BeautifulSoup(r.text,"lxml")
#创建bs4的对象
#print (soup.text)
print("#####test####")
#print(soup.prettify())

# ###page####
# store=[]
# for item in soup.find_all('div',attrs={'id': 'pagelist'}):
# 	print(item)
# store=item.find_all(attrs={'name': 'mp'})
# sumpage=int(store[0]['value'])
# print(sumpage)



print("#####test2####")
ch1=[]
ch2=[]
i=0
j=0
# for child1 in soup.find_all('span',attrs={'class': 'ct'}):
#     print('#'+str(child1.string)+"\n")
#     ch1=child1.string
#     print(ch1+ch[i])


# ######test ##########
# for child in soup.find_all('span',attrs={'class':'ctt'}):
# 	ch.append(str(child.text))

# for child1 in soup.find_all('span',attrs={'class':'ct'}):
# 	ch1.append(str(child1.string))
# 	i=i+1

# for times in range(0,i):
#   print("$"+ch[times]+"\n"+ch1[times]+"\n\n")


# print(ch[2])
# print(ch1[2])

print("it works!")



# #==============爬取关注用户===========
# #2186162277

# userid=input("Ready to spider the following user,input a target ID:\n爬取关注用户，请输入想要爬取的用户ID:\n")
# userid=int(userid)

# fo = open("%sfollowing users.text"%userid,"w")
# userlist=[]
# print("#######Spide following users#######")
# for page in range(1,15):
#     url2='https://weibo.cn/%s/follow?page=%d'%(userid,page)
#     r2 = requests.get(url2,cookies = cookie)
#     soup= soup=BeautifulSoup(r2.text,"lxml")
#     for child in soup.find_all('td',valign='top'):
#         print('#'+str(child.text))
#         userlist=child.text
#         fo.write("\n$ "+str(userlist)+"\n")




#print(soup.span.children)
#查找所有包含a的标签 e.g. <a href="XXXX" class="XXXX"> href，class均为属性
#print(soup.span.children.name)
#print(soup.a['href'])#输出tag a，属性为href的值
#print(soup.a.attrs)

# ##循环
# print("#####this LOOP####")
# for prttag in soup.find_all('a'):

#     #print(soup.a['href'])#输出tag a，属性为href的值
#     print(prttag.string) #put it first,it works.
#     prttag=prttag.get('href')
#     print(prttag)


#==============================爬取指定用户微博内容=============================
save=[]
store=[]
ch=[]

userid=input("Ready to spider the weibo content！！！\nPlz Input the userid:\n")
userid=str(userid)


url='https://weibo.cn/%s/profile?filter=0&page=1'%(userid)
r = requests.get(url,cookies = cookie)
soup=BeautifulSoup(r.text,"lxml")

###########页数############
for item in soup.find_all('div',attrs={'id': 'pagelist'}):
	print(item)
store=item.find_all(attrs={'name': 'mp'})
sumpage=int(store[0]['value'])
print("Page number:")
print(sumpage)


print(" Here we go>>>>>>>>>>>>>>>>>>>> ")

fo = open("filter1weibo_%s_content.text"%userid,"w")
fo.write("=================================================\n ")
fo.write("Weibo History:\n ")
fo.write("=================================================\n ")
for page in range(1,sumpage):
	url1='https://weibo.cn/%s/profile?filter=1&page=%d'%(userid,page)
	r1 = requests.get(url1,cookies = cookie)
	soup=BeautifulSoup(r1.text,"lxml")
	for child in soup.find_all('span',attrs={'class':'ctt'}):
		ch.append(str(child.text))
		print(str(child.text))
		i=i+1
	for child1 in soup.find_all('span',attrs={'class':'ct'}):
		ch1.append(str(child1.string))


	# for content in soup.find_all('span'):
	# #       #print(content)
	# #       #if you want to save the raw version plz open this comment blew:
	# #       #fo.write("\n[raw version]: "+str(content))
	# #       #print('#'+str(content.string)+"\n")
	# #       #save=content.string
	#     save=content.text
	#     print("$ "+str(save)+"\n")
	#     fo.write("$ "+str(save)+"\n")
	print("\n+++++++++++++加载第"+str(page)+"页+++++++++++++\n")
for times in range(0,i):
	if times<=1:
		fo.write("$"+ch[times]+"\n\n")
		print("$"+ch[times]+"\n\n")
	if times>1:
		fo.write("$"+ch[times]+"\n"+ch1[times-2]+"\n\n")
		print("$"+ch[times]+"\n"+ch1[times-2]+"\n\n")
#	fo.write("\n+++++++++++++加载第"+str(page)+"页+++++++++++++\n")

print("-------The end----------")






#start full version spider code:

# fo1 = open("weibo_XXX_Fullcontent.text","w")
# for page in range(1,10):
#  	url1='https://weibo.cn/xxx/profile?filter=1&page=%d'%(page)
#  	r1 = requests.get(url1,cookies = cookie)
#  	soup=BeautifulSoup(r1.text,"lxml")
#  	print("This is the user:XX`s weibo full content(display only 10 pages)")
#  	fo1.write("This is full content of the user:XX`s \n\n ")
#  	print("\n+++++++++++++这是第"+str(page)+"页+++++++++++++\n")
#  	fo1.write("\n+++++++++++++这是第"+str(page)+"页+++++++++++++\n")
#  #	print(soup.get_text())
#  	fo1.write("\n$"+soup.get_text())
