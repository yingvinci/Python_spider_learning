# On Learning Python Spider -spider pics 爬虫学习之爬取图片

## 0X00 Introduction

This tutorial is for Mac users learning python spider.


**相关配置**： 
 
*  Python 3.6.2   
*  Xcode,iTerm  
*  pip3,brew （安装方法见后文）  
*  第三方库：bs4（BeautifulSoup）, requests
*  lxml解析库
 
**安装方式**

<a>Python3 </a>

确定python的安装版本，一般来说Mac默认自带python 2.x。
>$python  --version
>$python3 --version


如果你的系统只安装了Python 2.X，或者已安装的Python 3版本较旧，可使用一个名为Homebrew的包来安装最新的Python 3版本


<a>安装Homebrew（注意：请将Xcode升级到最新版本！！！）</a>
>$`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
>  

为确认正确地安装了Homebrew，请执行如下命令:


>$ brew doctor
>
>>PS：可以忽略那些warnings,毕竟人家也说了"If everything you use Homebrew for is
working fine: please don't worry and just ignore them. Thanks! "

没什么问题的话（幸运的话），就可以继续安装python3.


>毕竟好多人都没开始python就已经倒在了出发点上（Especially for some OS users ，I was kidding^ ^ ）


<a>安装python3:</a>

为安装最新的Python 3版本并检查python的版本，请执行如下命令：

>$ brew install python3  
>$ python3 --version 

<a>lxml解析器</a>：

Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 lxml .根据操作系统不同,可以选择下列方法来安装lxml:
>$pip install lxml  
>$apt-get install Python-lxml

<a>哦对了，还有第三方库的安装：</a>
>$ pip install requests   
>$ pip install bs4




## 0X01 目的以及思路
爬取某网站当前页中所涉及的图片，并下载到本地计算机上。 
   
   **实现的思路：**
   首先要获取网页中的html信息，通过筛选html的标签来获取图片的URL存储到一个list中。然后通过list将图片下载到本地中。  
       
那么：    
1.如何获取网站的页面内容？  
2.得到完整页面的内容后，如何获取过滤数据，获取图片url？  
3.如何将图片下载到本地？

##0X02实现过程
###1.如何获取网站的页面内容？
利用requests库，几行代码就可以实现. 
  
基础科普：

首先导入 requests 库

``` 
>import requests

```
*requests.get(url,parm,headers)*函数：获取某个某个网页,参数`parm` 和`headers`可以为空，参数`url` 为目标的网址。

```
>>requests.get(url,parm,headers)
```
获取虾米网首页的内容例子如下：

```
r = requests.get("http://www.xiami.com/")
```
运行之后会出现如下的错误：

```
<h1>400 Bad Request</h1>
<p>Your browser sent a request that this server could not understand. Sorry for the inconvenience.<br/>
Please report this message and include the following information to us.<br/>
Thank you very much!</p>
```
那是什么原因呢？啊哈，因为要模拟浏览器，原来是缺乏header参数的配置。那么就模拟一下浏览器参数的配置吧！

```
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '     
                    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
     'Referer': 'http:/xiami.com,
      'Connection': 'keep-alive'
  }
  
```
 
 这样将header参数配置好之后，在运行一下就OK啦。  
**Here is code:**

```
#spider.py#
import requests 
payload = {} 

headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '     
                    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
     'Referer': 'http:/xiami.com,
      'Connection': 'keep-alive'
  }
  
r = requests.get("http://www.xiami.com/", params=payload, headers=headers)
print(r.text)

```

### 2.得到完整页面的内容后，如何获取过滤数据，获取图片url？

那就需要介绍一下bs4啦：  
  
>Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
> >  Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
>>> Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。


In short 利用bs4可以更方便快捷地筛选数据。^ ^
快速介绍bs4的基本用法：

Python3的导入方式：   
`from bs4 import BeautifulSoup`  

创建一个soup实例：
soup=BeautifulSoup(r.text,"lxml")



### <a>3.重点来了，如何过滤将网页中的标签呢？</a>：  


***
<a name="2">科普</a>： 
 
* 搜索文档树  

find_all()方法搜素当前tag的所有tag子节点,并判断是否符合过滤器的条件。
  
  
Option name         | code           | 
--------------------|------------------|
搜索`<div>`标签       | Soup.find_all('div')   | 
搜索`<a>`标签       | Soup.find\_all('a')   | 
搜索`<div>`和`class类为imag`的标签  | soup.find\_all('div',class_='image')      | 
Quote [^quote]      | \"Such editor\"  | <q>Such editor</q>    |
Highlight           | \==So good\==    | <mark>So good</mark>  |

  
搜索`<div>`标签 :   
`>Soup.find_all('div')`

搜索`<a>`标签  
  
`>Soup.find_all('a')    `

搜索`<div>`和`class类为imag`的标签  

`>soup.find_all('div', class_='image')  `

关于更多的bs的内容参见官方文档[Beautiful Soup 4.4.0 文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/)

***

那么利用强大的bs4我们就很容的筛选出我们想要的url。首先浏览html页面
发现image的url都在div标签的子节点下

Here is code:

```
img_src=[]#创建一个空的列表
i=0 #flag i
for myimg in soup.find_all('div', class_='image'):
#在所有包含 div 以及 class_=image 的标签中进行for循环
     img_src = myimg.find('img').get('src')#继续筛选，将img 标签中的src中的内容存储到img_src中。
     pic_name=str(i)+".jpg"  #将图片的名字设1.jpg，2.jpg以此类推
     request.urlretrieve(img_src, pic_name)  
     i+=1   
     print(img_src)   #打印img_src中存储的内容
```

那么这样的话，运行之后。经过筛选的图片的url都存储在列表img_src当中，里成功还差一步之遥。那么如何将图片下载到本地？
通过python3自带urllib库的方法将图片下载到本地：

 一般用法

```
form urllib import request
img_url="http:///.....""
request.urlretrieve(img_url, path)
#path为自定义路径，不设置路径（如img_url,1.jpg），则文件被命名为1.jpg自动保存到代码所在文件夹下。

```
实际：

```
pic_name=str(i)+".jpg"  #将图片的名字设1.jpg，2.jpg以此类推
request.urlretrieve(img_src, pic_name)

```



## 0X03完整代码
 Here is the code:

```
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
```
## 0X04NEXT
* 之后可继续深入的地方：
* 对全站进行图片爬取
* 对动态页面进行爬取
* etc.

## 0X05Reference

1. Beautiful Soup 4.4.0 文档 http://beautifulsoup.readthedocs.io/zh_CN/latest/
2. 《Python 编程：从入门到实践》
3. Requests http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
4. Liezblogs http://www.cnblogs.com/liez/p/5399967.html
4. X剑豪blogs http://www.cnblogs.com/xjianhao/p/5810189.html
5. 崔庆才 blogs http://cuiqingcai.com/1319.html
6. 李祥 blogs http://www.cnblogs.com/MyNameIsMT/p/5426664.html



