import re
from bs4 import BeautifulSoup
import urllib.request
import xlwt

def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = ".250豆瓣排行耪.xls"
    datelist = askDate(baseurl)
    saveDate(datelist,savepath)

 #创建正则表达式对象
linkhref = re.compile(r'<a href="(.*?)">',re.S)#得到电影的链接
linkbd = re.compile(r'<div class="bd"><p class="">(.*?)</p>',re.S)
linktitle = re.compile(r'<span class="title">(.*?)</span>')

#得到指定的url,以及解析html
def askDate(baseurl):
    datelist = []
    datelist1 = []
    for i in range(0,10):
        url = baseurl+str(i*25)
        html = getDate(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            item = str(item)
            href = re.findall(linkhref,item)[0]
            datelist1.append(href)
            title = re.findall(linktitle,item)
            if len(title)>1:
                datelist1.append(title[0])
                datelist1.append(title[1].replace("/",""))
            else:
                datelist1.append(title[0])
                datelist1.append(" ")
            datelist.append(datelist1)
            datelist1 = []
    return datelist


#向网页发送请求，
def getDate(url):
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"}
    reg = urllib.request.Request(url,headers=head)
    datelist = []
    html = ''
    try:
        response = urllib.request.urlopen(reg)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,code):
            print(e.code)
        if hasattr(e,reason):
            print(e.reason)
    return html

#保存数据
def saveDate(datelist,savepath):
    work = xlwt.Workbook(encoding = "utf-8")
    sheet = work.add_sheet("250豆瓣排行榜",cell_overwrite_ok = True)
    col = ("链接","中文名字","外国名字")
    for i in range(len(col)):
        sheet.write(0,i,col[i])
    for j in range(len(datelist)):
        date = datelist[j]
        for k in range(len(date)):
            sheet.write(j+1,k,date[k])
    work.save(savepath)#保存文件

if __name__ == "__main__":
    main()
    print("爬取完成")
