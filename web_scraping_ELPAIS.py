import requests
import csv
from bs4 import BeautifulSoup

#get function is used to access the URL, where web scraping is applied.
result=requests.get("https://www.elpais.com")

#We check whether request is successful
print(result.status_code)

#We save the extracted content in src
src=result.content

#Once the analyzed page is stored, the library BeautifulSoup  is used
#to parse the stored HTML document. Through the attribute
# 'html5lib' is told what type of document to be analyzed.
soup=BeautifulSoup(src,'html5lib')


#Through source code of the URL inspection 
#you see that the headlines you want to extract are contained in <a> elements
#under the label 'h2' and with the attribute class = 'article-title'. Therefore through
#following function all elements 'h2' whose attribute is accessed
# class = 'article-titulo'
text=soup.find_all('h2', class_='articulo-titulo')

list_titles = []

#A document '.csv' is opened
with open("web_scraping_export.csv", "w") as ws_file:

#Through a 'for' loop is possible to access all <a> elements contained in 'text' object.
#'get_text()' is used to access the text contained in <a> element.
    for h2_tag in text:

        title = h2_tag.find('a').get_text()
        #Con las siguientes sentencias se escribe de forma iterativa en el fichero '.csv' abierto
        #anteriormente
        ws_file.write(title)
        ws_file.write(';')
        #Se guarda el contenido accedido en el vector list_titles.
        list_titles.append(title)

#We close '.csv' file
ws_file.close()

#-----------
#Reference
#-----------

#https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
#https://github.com/vprusso/youtube_tutorials/tree/master/web_scraping_and_automation/beautiful_soup
#https://stackoverflow.com/questions/37289951/python-write-to-csv-line-by-line
#https://github.com/rafoelhonrado/foodPriceScraper/blob/master/foodPriceScraper.py
#https://github.com/datalifecicleuoc/web-scraping
#https://guides.github.com/activities/hello-world/
#https://www.youtube.com/watch?v=87Gx3U0BDlo
#https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211
#https://elpais.com/
#https://elpais.com/robots.txt
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
