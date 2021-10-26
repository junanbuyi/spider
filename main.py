import requests
from bs4 import BeautifulSoup
import re
import time
'''
思路：获取网址
      获取图片地址
      爬取图片并保存
'''
def getUrl(url):
    try:
        time.sleep(2)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'}
        read = requests.get(url,headers= headers,timeout = 3)  #获取url
        read.raise_for_status()   #状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
        return read.text    #Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"
 
# 获取图片地址并保存下载
def getPic(html):
    j=0
    soup = BeautifulSoup(html_url, "html")
    all_img = soup.find_all("img") 
    #通过分析网页内容，查找img的统一父类及属性
    for img in all_img:
        print(4)
        img_url = img.get("src")
        print(type(img_url))
        root = "F:/4.pycharm/"   #保存的路径
        path = root + str(j)+".jpg" #获取img的文件名
        j+=1
        print(img_url)
        with open(path,'wb+') as f:
            all_img2 = requests.get(""+img_url)#获取href
            f.write(all_img2.content)
            print(1)
# 主函数
if __name__ == '__main__':
   html_url=getUrl("")#输入url
   getPic(html_url)
