
from bs4 import BeautifulSoup 
import requests
import json
import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")


def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")


    movie_r=[]
    movie_n=[]
    year_release=[]
    m_urls=[]
    m_rating=[]

    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "." not in i:
                rank=rank+i
            else:
                break
        movie_r.append(rank)


        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_n.append(title)

        y=tr.find("td",class_="titleColumn").span.get_text()
        
        year_release.append(y)
    

        mr=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        m_rating.append(mr)

        link=tr.find("td",class_="titleColumn").a["href"]
        m_l="https://www.imdb.com"+link
        m_urls.append(m_l)

    top_movies=[]
    d={}
    for i in range(len(movie_r)):
        d["position"]=int(movie_r[i])
        d["name"]=str(movie_n[i])
        year_release[i]=year_release[i][1:5]
        d["year"]=int(year_release[i])
        d["rating"]=float(m_rating[i])
        d["url"]=m_urls[i]
        top_movies.append(d)
        d={}
        # return top_movies

    with open("task1.json","w")as f:
        json.dump(top_movies,f,indent=4)

(scrap_top_list())
# import pprint
# pprint.pprint(scrap_top_list())





