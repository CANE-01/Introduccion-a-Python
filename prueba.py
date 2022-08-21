#Prueba modulo Introduccion a la programacion. Autor: Cristobal Novoa Espejo

#Se importan librerías json y requests

import json
import requests

#Se generan variables url_nasa y params_nasa 

url_nasa = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos'

params_nasa = {'api_key': '1eWoNZ5gxVikzKUNAzZBEm7fGbhCgcOx2iAZqzx9'}

#Se genera la solicitud a la api y se convierte la informacion en un objeto de python

response = requests.request("GET", url = url_nasa, params = params_nasa)

results = json.loads(response.text)

#Se genera la variable data que se queda solo con los quince primeros registros

data = (results['latest_photos'][0:15])
#print(data)
##################################################################################################################

#Se genera lista de urls solo con las imagenes encontradas

lista_urls = []

for i in data:
    lista_urls.append(i["img_src"])

#print(lista_urls)

###################################################################################################################

#Se genera funcion para crear pagina web con imagenes obtenidas usando variable html, a la cual se le van concatenando las etiquetas

def build_web_page(lista_urls):
    html = "<html>\n<head>\n</head>\n<body>\n<ul>\n"

#Se usa el ciclo para agregar las imagenes a la pagina web

    for photo in lista_urls:
        html += "\t<li><img src=\"{}\"></li>\n".format(photo)

    html += "</ul>\n</body>\n</head>\n</html>"


#Se genera archivo html

    with open("output.html", "w") as f:
        return f.write(html)

    

