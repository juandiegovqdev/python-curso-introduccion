# -*- coding: utf-8 -*-

from centros import *

def mostrar_numerados(centros):
    for n,e in enumerate(centros):
        print (n,"-", e)

def test_num_total_camas_centros_accesibles(centros):
    total_camas_accesibles = num_total_camas_centros_accesibles(centros)
    print('El numero total de camas de los centros accesibles es', total_camas_accesibles)

def test_centros_con_uci_cercanos(centros):
    latitud =36.52016726032299 
    longitud = -6.151330284937666
    print ('Los centros cercanos a las coordenadas ({},{})  son'.format(latitud, longitud))
    cercanos = centros_con_uci_cercanos(CENTROS, (latitud, longitud), 0.2)
    print (mostrar_numerados(cercanos))
    generar_mapa(cercanos, "../out/mapa_centros_cercanos.html")    

def test_media_coordenadas (centros):
    latitud =36.52016726032299 
    longitud = -6.151330284937666
    cercanos = centros_con_uci_cercanos(centros, (latitud, longitud), 0.2)   
    media = media_coordenadas(cercanos)
    print ('La media de las coordenadas de los centros es({},{})  son'.format(media[0], media[1]))
        
if __name__=="__main__":   
    CENTROS = lee_centros()
    test_num_total_camas_centros_accesibles(CENTROS)