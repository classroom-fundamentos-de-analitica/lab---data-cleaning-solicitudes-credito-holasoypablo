"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.dropna(inplace=True)

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace('_',' ')
    df.idea_negocio = df.idea_negocio.str.replace('-',' ')

    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('_',' ')
    df.barrio = df.barrio.str.replace('-',' ')

    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace('_',' ')
    df.línea_credito = df.línea_credito.str.replace('-',' ')

    df.comuna_ciudadano=df.comuna_ciudadano.astype(int)

    df.estrato=df.estrato.astype(int)

    df.fecha_de_beneficio = [datetime.strptime(date, "%d/%m/%Y") if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date)) else datetime.strptime(date, "%Y/%m/%d") for date in df.fecha_de_beneficio]

    df.monto_del_credito = df.monto_del_credito.str.replace('$ ','')
    df.monto_del_credito = df.monto_del_credito.str.replace('.00','')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(int)

    df.drop_duplicates(inplace=True)

    print(df)
    return df

print('\n-----------------------------Hecho por Juan Pablo Buitrago Diaz CC 1000.206.552-----------------------------\n')
df = clean_data()
print(df.sexo.value_counts(),'\n')
#print(df.tipo_de_emprendimiento.value_counts(),'\n')
#print(df.idea_negocio.value_counts().to_string(),'\n')
#print(df.barrio.value_counts().to_string(),'\n')
#print(df.estrato.value_counts().to_string(),'\n')
#print(df.comuna_ciudadano.value_counts().to_string(),'\n')
#print(df.fecha_de_beneficio.value_counts().to_string(),'\n')

