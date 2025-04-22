#script para extraer los hashes del virus, en la columna details, se uso la libreria vt-py
#Author: Raul Villano Obregon
#Fecha:11-06-2024
#Version: 1.0

import vt
import pandas as pd
import numpy as np
import openpyxl

api_key='7c5b0431172a75f49154e0a81c07520f72fc18f210f79624720181c0ada26b79'          #apikey
client = vt.Client(api_key)                                                         #creando cliente de la api
cve=input('ingresa el hash a validar: ')                                            #ingresando el hash
ruta='/files/'+cve                                                                  #construyendo la url del hash
file = client.get_object(ruta)                                                      #extrayendo el file de la api en json
#etraccion de hashes
sha256=file.sha256
md5=file.md5
tlsh=file.tlsh
ssdeep=file.ssdeep
vhash=file.vhash
imphash=file.pe_info['imphash']
sha1=file.sha1
authentihash=file.authentihash
hashes=[md5,sha1,sha256,vhash,authentihash,imphash]                                 #creacion de lista de hashes
df=pd.DataFrame(hashes)                                                             #creando dataframe de hashes
dft=np.transpose(df)                                                                #pasanod de filas a columnas
#cambiando el nombre de las columnas
dft.rename(columns={0: 'md5', 1: 'sha1', 2: 'sha256', 3: 'vHash',4: 'autentiHash',5:'imphash'}, inplace=True, errors='raise')
dft.to_excel('hashes.xlsx', index=False)                                            #exportando a excel
print(dft)