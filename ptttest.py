#for git test
from urllib.request import urlopen,Request
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup as bs

url="https://www.ptt.cc/bbs/movie/M.1663938818.A.AC1.html"
# r=Request(url)
# r.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0")
# response= urlopen(r)

response=requests.get(url,cookies={"over18":"1"})
html=bs(response.text,"lxml")

content=html.find("div",id="main-content")
metas=content.find_all("span",class_="article-meta-value")
# print(metas[0])
print(content)
ms=content.find_all("div",class_="article-metaline")

for m in ms:
    m.extract()
print(content)


