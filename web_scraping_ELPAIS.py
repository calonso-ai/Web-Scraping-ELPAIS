import requests
import csv
from bs4 import BeautifulSoup

#Se usa la función get para acceder a la URL donde se desea hacer web scraping
result=requests.get("https://www.elpais.com")

#Se comprueba que el resultado de la petición es correcto, por lo tanto el acceso
#a la web será satisfactorio
print(result.status_code)

#A continuación se almacena el contenido de la página web accedida en una variable
src=result.content

#Una vez se tiene almacenada la página que se quiere analizar, se usa la librería
#BeautifulSoup para analizar el documento HTML almacenado.A través del atributo
#'html5lib' se le indica que tipo de documento se quiere analizar.
soup=BeautifulSoup(src,'html5lib')

#A través de la inspección del código fuente de la URL indicada anteriormente
#se ve que los titulares que quieren extraerse están contenidos en elementos <a>
#bajo la etiqueta 'h2' y con el atributo class='articulo-titulo'. Por lo tanto a través
#de la siguiente función se acceden a todos los elementos 'h2' cuyo atributo
#class='articulo-titulo'
text=soup.find_all('h2', class_='articulo-titulo')

list_titles = []

#A continuación se abre un documento '.csv' 
with open("web_scraping_export.csv", "w") as ws_file:

#Y se usa un bucle 'for' para acceder a los elementos <a> contenidos en el objeto 'text'.
#Se usa la función 'get_text()' para acceder al text almacenado en el elemento <a>.
    for h2_tag in text:

        title = h2_tag.find('a').get_text()
        #Con las siguientes sentencias se escribe de forma iterativa en el fichero '.csv' abierto
        #anteriormente
        ws_file.write(title)
        ws_file.write(';')
        #Se guarda el contenido accedido en el vector list_titles.
        list_titles.append(title)

#Una vez finalizado el bucle, se han accedido a todos los elemento y se han volvado en el fichero '.csv'
#se cierra el fichero '.csv' en cuestión.
ws_file.close()

#-----------
#REFERENCIAS
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
