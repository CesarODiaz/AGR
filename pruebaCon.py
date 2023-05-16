# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Cesar Diaz
"""
import pandas as pd
#import psycopg2

#con = psycopg2.connect(
#    database="SIAObservaV1_CLOUD_2022_10_31-INCIDENTES",
#    user="AGR\jlombana",
#    password="Auditoria2023+",
#    host="SQLBOGAGR02DES",
#    port='5432'
#    )
import pyodbc 

con = pyodbc.connect('Driver={SQL Server};'
                      'Server=SQLBOGAGR02DES;'
                      'Database=SIAObservaV1_CLOUD_2022_10_31-INCIDENTES;'
                      'Trusted_Connection=yes;')
#cursor = con.cursor()
#cursor.execute("SELECT * FROM CONTRATO")
#cursor.execute("SHOW TABLES")
query = "SELECT * FROM DOCUMENTO"
df4 = pd.read_sql(query, con)

#df es CONTRATO_SUPERVISORES_LOG
#df1 es CONTRATO
#df2 es CONTRATO_CDPS
#df3 es CONTRATO_CDP
#df4 es DOCUMENTO

#for x in cursor:
#    print(x)

df4_Documento = df4.query("DOCUMENTO_NAME == 'ESTUDIOS PREVIOS' | DOCUMENTO_NAME == 'ESTUDIOS PREVIOS(AGR)' | DOCUMENTO_NAME == 'Estudios Previos'")
df5_Doc_HV = df4[df4['DOCUMENTO_NAME'].str.contains('HOJA DE VIDA')]
df6_Doc_HV_Sop = df4[df4['DOCUMENTO_NAME'].str.contains('SOPORTE')]
df4_Doc_Ant = df4[df4['DOCUMENTO_NAME'].str.contains('Anteceden') & df4['DOCUMENTO_NAME'].str.contains('Fiscal')]

