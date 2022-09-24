from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup
import pandas as pd

df=pd.DataFrame(columns=["JA","EN","Score"])
page = 55
while True:
    url = f"https://tabelog.com/tw/tokyo/rstLst/{page}/?SrtT=rt"
    print(url)
    try:
        response=urlopen(url)
    except HTTPError:
        break

    html= BeautifulSoup(response)
    # print(html)

    for r in html.find_all("li",class_="list-rst"):
        ja=r.find("small",class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        print(ja.text,en.text,en["href"])
        rating=r.find("b",class_="c-rating__val")
        s=pd.Series([ja.text,en.text,rating.text],index=["JA","EN","Score"])
        df= df.append(s,ignore_index=True)
        # ratings=r.find_all("b",class_="c-rating__val")
        # for rating in ratings:
        #     print(rating.text)
    page+=1

df.to_csv("tables.csv",encoding="utf-8",index=False)
