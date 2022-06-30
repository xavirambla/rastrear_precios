#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.es/ZOTAC-Gaming-GeForce-GTX-Tarjeta/dp/B07YVHCD8Q/ref=sr_1_148?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1UE976VDM9VOO&dchild=1&keywords=tarjeta+gr%C3%A1fica+8gb&qid=1619622233&sprefix=tarjeta+grafica%2Caps%2C189&sr=8-148'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


class Rastreador():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


    def rastrear_precio(self, url):
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        producto = soup.find(id="productTitle").get_text().strip()
 #       print("PRoducto : {0}    Precio : -".format(producto))
        precio = soup.find(id="priceblock_ourprice").get_text().strip()
#        print("PRoducto : {0}    Precio : {1}".format(producto,precio))
#        precio = precio.replace(" €","")
        #        print(":{0}:".format(precio))
        #        print("{0}".format(precio[:-2]))
        #        print("{0}".format(precio[3:]))
        precio_aux= precio[:-2]
        precio_aux = precio_aux.replace(",",".")
        precio_convertido = float(precio_aux)
        return producto,precio


    def check_precio(self,url,precio_aviso):
        producto,precio = self.rastrear_precio(url)
        if (precio < precio_aviso):
            self.enviar_correo(producto, precio)


    def enviar_correo(self, producto, precio):
        fromaddr = 'xavirambla@gmail.com'
        toaddrs = 'xavirambla@yahoo.es'

        # Datos
        username = 'xavirambla@gmail.com'
        password = 'lisboa01.'

        # Enviando el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)

        subject = 'El precio bajo'
        body = 'Revisar el siguiente link de amazon: ' + URL

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            fromaddr,
            toaddrs,
            msg
        )
        print("HEEEEEY, el producto bajo")
        server.quit()

token = "B074JCXNLF"

lista=[
    { 'url':"https://www.amazon.es/Bestway-56404-Steel-propool-Marco-Acero/dp/B07BHMGNV7/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1XKXCGXOFSQ48&dchild=1&keywords=piscinas%2Bdesmontables&qid=1619645193&sprefix=piscina%2Caps%2C185&sr=8-1-spons&smid=AY045PXBS2YWW&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSkxZSjNGU0RESkQmZW5jcnlwdGVkSWQ9QTA3NjM5MjIzSTFUTkdHSjBTQUQmZW5jcnlwdGVkQWRJZD1BMDU2MTcxMzFCTFJBUjBYQVA3N1Qmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1",     'precio_aviso':100},
    { 'url':'https://www.amazon.es/Port%C3%A1til-Tokmali-Ajustable-Ordenadores-Port%C3%A1tiles/dp/B088C45T35/ref=pd_rhf_se_s_sspa_dk_rhf_search_pt_sub_1_5/258-1716641-6824700?_encoding=UTF8&pd_rd_i=B088C45T35&pd_rd_r=092bdbc1-8321-4730-af4c-8019ebdb751a&pd_rd_w=UuFNv&pd_rd_wg=aTg0m&pf_rd_p=cd473fbf-6a2b-4e4e-a50c-ef0f45496a6d&pf_rd_r=1138K3TTYX76GAZ7GRHN&psc=1&refRID=1138K3TTYX76GAZ7GRHN&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQ05UNVZXUDBDT0dUJmVuY3J5cHRlZElkPUEwOTg5MTIzMzRXMFhKS1k4Uk5HRSZlbmNyeXB0ZWRBZElkPUEwNjU3MDY1M1BCTU9XUFg5V1kySSZ3aWRnZXROYW1lPXNwX3JoZl9zZWFyY2gmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl', 'precio_aviso':10    } ,
    { 'url':'https://www.amazon.es/ZOTAC-Gaming-GeForce-GTX-Tarjeta/dp/B074JCXNLF/ref=sr_1_148?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1UE976VDM9VOO&dchild=1&keywords=tarjeta+gr%C3%A1fica+8gb&qid=1619622233&sprefix=tarjeta+grafica%2Caps%2C189&sr=8-148' , 'precio_aviso':10 }
]



rastreador = Rastreador()


for element in lista:
    producto,precio = rastreador.rastrear_precio(element['url'])
    print("{0} - {1} ** {2} {3}".format(producto,precio,element['precio_aviso'],element['url']))
#    rastreador.check_precio(URL,element['precio_aviso'])


"""
while True:
    rastrear_precio()
    time.sleep(20)
"""