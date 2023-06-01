#Autores: Sofia S.- Hernàn V. - Roberto B.

import pandas as pd


# Lectura el archivo TyP2022.csv
df = pd.read_csv('TyP2022.csv')

mes_dict = {'Enero': '01', 'Febrero': '02', 'Marzo': '03', 'Abril': '04'
              , 'Mayo': '05', 'Junio': '06', 'Julio': '07', 'Agosto': '08'
              , 'Septiembre': '09', 'Octubre': '10', 'Noviembre': '11'
              , 'Diciembre': '12'}

df['Mes'] = df['Mes'].map(mes_dict)


df['Mes'] = pd.to_datetime(df['Mes'], format='%m')


# Ciudad con temperatura máxima
ciudad_max_temp = df.loc[df['Temperatura'].idxmax()]['Ciudad']

# Ciudad con temperatura mínima
ciudad_min_temp = df.loc[df['Temperatura'].idxmin()]['Ciudad']

# Calculando la temperatura promedio trimestral
df['Trimestre'] = pd.PeriodIndex(df['Mes'], freq='Q')
df['Trimestre'] = 'Trimestre' + df['Trimestre'].dt.quarter.astype(str)
promedio_trimestral = df.groupby(['Trimestre'])['Temperatura'].mean().iloc[1:]



# Total de agua caída en mm
cantidad_agua = df['Precipitación'].sum()

# Mostrar los resultados por consola
print('Ciudad con temperatura máxima:', ciudad_max_temp)
print('Ciudad con temperatura mínima:', ciudad_min_temp)
print('Temperatura promedio trimestral en ºC:\n', promedio_trimestral)
print('Cantidad total de agua caída en:', cantidad_agua,'mm')