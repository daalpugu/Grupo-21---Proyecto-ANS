#!/usr/bin/env python
# coding: utf-8

# # Desnutrición Aguda en Menores de 5 Años - Análisis preliminar de los datos
# 
# 
# 

# Registro de pacientes atendidos en las Instituciones Prestadoras de Servicios de Salud con diagnóstico confirmado de Desnutrición Aguda en menores de 5 años y notificados al SIVIGILA desde el año 2016 al 2021.

# In[38]:


# Importar librerías
import pandas as pd
import seaborn as sns
import requests
import json
import matplotlib.pyplot as plt


# In[39]:


# URL directa del archivo JSON
url = 'https://raw.githubusercontent.com/daalpugu/Grupo-21---Proyecto-ANS/main/data/sivigila_Desnutricion.json'

# Hacer una solicitud GET para obtener el contenido del archivo
response = requests.get(url)

# Cargar el contenido en un objeto JSON
var_des = json.loads(response.text)

# Abrir el archivo de descripción de variables en modo lectura (r) *Para la opción de repositorio local
#with open('https://raw.githubusercontent.com/daalpugu/Grupo-21---Proyecto-ANS/main/data/sivigila_Desnutricion.json', 'r') as file:
#    var_des = json.load(file)

# Convertir el diccionario en DF
df_var_des =  pd.DataFrame(var_des['fields'])

# Permitir que se muestre todo el contenido de la variable
pd.set_option('display.max_colwidth', None)

# Resetear la opción de mostrar todo el contenido de las variables
# pd.reset_option('display.max_colwidth')

df_var_des[['name','description']]


# In[35]:


# Cargar la base de datos desde el repositorio en Github
url = 'https://raw.githubusercontent.com/daalpugu/Grupo-21---Proyecto-ANS/main/data/sivigila_desnutricion.csv'
df = pd.read_csv(url)


# In[36]:


print(f"El tamaño de la base es: {df.shape}")
df.head()


# In[8]:


df.tail()


# In[9]:


# Ajustar las variables decimales, porque hay números con . y otros con ,
df['talla_nac'] = df['talla_nac'].str.replace(',','.')
df['peso_act'] = df['peso_act'].str.replace(',','.')
df['talla_act'] = df['talla_act'].str.replace(',','.')
df['per_braqu'] = df['per_braqu'].str.replace(',','.')

df['talla_nac'] = df['talla_nac'].astype(float)
df['peso_act'] = df['peso_act'].astype(float)
df['talla_act'] = df['talla_act'].astype(float)
df['per_braqu'] = df['per_braqu'].astype(float)

df.tail()


# In[10]:


df.info()


# In[11]:


'''Teniendo en cuenta que la variable edad puede estar en días, meses o años,
se crea una nueva variable de edad estandarizada en meses para mejor interpretabilidad'''

# Crear una función para calcular la edad en meses
def edad_meses(fila):
  if fila['uni_med_'] == 1:
    return fila['edad_']*12 # si la edad está en años multiplicar x12 meses
  elif fila['uni_med_'] == 2:
    return fila['edad_']    # si la edad está en meses dejar el mismo valor
  elif fila['uni_med_'] == 3:
    return (round(fila['edad_']/30, 2)) # si la edad está en días, dividir en 30 días y redondear a 2 decimales
  else:
    return None # si no se cumple ninguno de los casos anteriores

# Crear la variable edad_mes
df['edad_mes'] = df.apply(edad_meses, axis=1) # aplicar la función anterior a las filas
df.head()


# In[12]:


df['edad_mes'].dtype


# In[13]:


# Nuevo df sin variables edad_, uni_med_

df_1 = df.drop(columns=['edad_', 'uni_med_'])
df_1.head()


# In[40]:


# Estadísticas descriptivas variables numéricas
descriptivas = df_1.describe(include='all')
descriptivas.T


# In[53]:


# Gráfico de barras de las variables: sexo, paciente hospitalizado, esquema de vacunación y año

cols_1 = ['sexo_', 'pac_hos_', 'esq_vac', 'year_', 'tipo_ss_']

n_cols = 5
n_filas = 1
fig,axes = plt.subplots(figsize=(15, 6))

for posicion,variable in enumerate(cols_1):
        aux_lista_valores = df_1[variable] #extrae los valores de la variable
        aux_llaves = aux_lista_valores.unique()
        aux_llaves.sort()
        conteo = []
        for j in aux_llaves:
            aux = aux_lista_valores.tolist().count(j)
            conteo.append(aux)

        plt.subplot(n_filas, n_cols, posicion + 1)
        plt.subplots_adjust(hspace=1.5, wspace= .5) #espacio entre filas
        plt.bar(aux_llaves,conteo, color="darkslateblue")
        plt.title(variable)
        plt.xticks(rotation=45,fontsize=7)
plt.show()


# In[54]:


# Histogramas de las variables: 'peso_act', 'talla_act', 'per_braqu' y 'edad_mes'

cols_2 = ['peso_act', 'talla_act', 'per_braqu', 'edad_mes']

n_cols = 4
n_filas = 1
fig,axes = plt.subplots(n_filas, n_cols, figsize=(15, 6))

for posicion,variable in enumerate(cols_2):
        ax = axes[posicion]
        aux_lista_valores = df_1[variable] #extrae los valores de la variable
        plt.subplot(n_filas, n_cols, posicion + 1)
        plt.subplots_adjust(hspace=1.5) #espacio entre filas
        plt.hist(aux_lista_valores, edgecolor = "k", bins=15, color = 'darkslateblue')
        plt.title(variable)
        xticks = ax.get_xticks()
        interval = max(1, len(xticks) // 10)  # Evitar división por cero
        ax.set_xticks(xticks[::interval])
        ax.set_xticklabels(ax.get_xticks(), rotation=45, fontsize=7)

plt.show()


# In[30]:


num_ceros = (df['per_braqu'] == 0).sum()
print(f"Número de valores igual a 0 variable 'per_braqui': {num_ceros}")
num_ceros = (df['peso_nac'] == 0).sum()
print(f"Número de valores igual a 0 variable 'peso_nac': {num_ceros}")
num_ceros = (df['peso_nac'] == 5000).sum()
print(f"Número de valores igual a 5000 variable 'peso_nac': {num_ceros}")
num_ceros = (df['talla_nac'] == 0).sum()
print(f"Número de valores igual a 0 variable 'talla_nac': {num_ceros}")
num_ceros = (df['edad_ges'] == 0).sum()
print(f"Número de valores igual a 0 variable 'edad_ges': {num_ceros}")
num_ceros = ((df['peso_nac'] == 0) & (df['talla_nac'] == 0) & (df['edad_ges'] == 0)).sum()
print(f"Número de registros con 0 en las variables 'edad_ges', 'peso_nac' y 'talla_nac': {num_ceros}")


# In[49]:


# Análisis de correlaciones entre variables numéricas:

# Se pasa la variable categórica 'sexo_' a una variable númerica para analizar su correlación con otras
df_1['sexo_'] = df_1['sexo_'].map({'M': 0, 'F': 1})
# Filtrar solo las columnas numéricas
df_numericas = df_1.select_dtypes(include=['float64', 'int64'])
df_numericas = df_numericas.drop(columns=['id', 'semana', 'year_', 'tip_cas_'])

# Calcular la matriz de correlación
matriz_correlacion = df_numericas.corr()

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 8))

# Crear el mapa de calor con valores numéricos
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Mostrar el gráfico
plt.show()


# In[ ]:




