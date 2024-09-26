# Grupo-21---Proyecto-ANS
Aprendizaje No Supervisado en la Identificación de Patrones de Desnutrición Infantil en Medellín

# Introducción
El problema de desnutrición infantil en Medellín afecta gravemente a los niños menores de cinco años, impactando su desarrollo físico y cognitivo. Este proyecto busca determinar: ¿Cómo las técnicas de Clustering basadas en variables de salud y nutrición pueden identificar perfiles de desnutrición en esta población? La respuesta permitiría gestionar políticas públicas más efectivas y dirigidas, optimizando la asignación de recursos. 

En el contexto organizacional de la salud pública en Medellín, es crucial entender mejor las formas de desnutrición para diseñar intervenciones adecuadas. A nivel internacional, estudios como los de Striessnig y Bora (2019) en India han usado PCA y Clustering para identificar patrones de malnutrición basados en factores como el acceso a los recursos y educación. Leyso y Palatino (2020), en Filipinas, aplicaron modelos de escaneo espacial para identificar Clusters de bajo peso y sobrepeso. En Etiopía, Bitew et al. (2021) usaron modelos de Machine Learning como XGBTree y K-Nearest Neighbours para predecir factores claves de desnutrición. 

Por otro lado, en Colombia, Castillo y Suarez.Ortegón (2023) investigaron la malnutrición infantil utilizando regresión logística, identificando factores demográficos importantes. Loaiza et al (2023), en Medellín, emplearon minería de datos y Machine Learning para encontrar correlaciones entre condiciones sociales y de salud. 

Aun cuando varios de los estudios anteriores utilizaron desde modelos de regresión hasta Machine Learning para identificar factores de riesgo y patrones de malnutrición, las limitaciones radican en la necesidad de contar con datos precisos y actualizados. Este proyecto se centra específicamente en la aplicación de técnicas de Clustering para agrupar poblaciones según características similares de desnutrición, permitiendo una intervención más dirigida y personalizada por las autoridades de salud en Medellín. 

Se utilizan las siguientes carpetas 

# data: Contiene todos los conjuntos de datos utilizados o generados durante el proyecto.
Posee los archivos base con los cuales se realiza la revisión preliminar de los datos, sivigila_Desnutricion.json, esta base cuenta con el diccionario de las variables que posee la base de datos sivigila_desnutricion.csv.

# src: Scripts de código fuente para procesamiento y análisis de datos.
Posee scrips del código relacionado, con la lectura de las bases que se encuentran en la carpeta, posterior a esto código relacionado con el análisis preliminar de los datos contenidos en la base de datos sivigila_desnutricion.csv.

# docs: Documentación adicional y reportes relacionados con el proyecto.
Posee el archivo .pdf en donde se expresa el contenido que sustenta el desarrollo del proyecto, el mismo cuenta con: Resumen, Introducción, Revisión preliminar de la literatura, Descripción de los datos, Propuesta metodológica, Bibliografía.

# notebooks: Jupyter Notebooks para una visualización interactiva de los análisis, junto con los resultados obtenidos de los análisis, incluyendo gráficos y tablas.
Posee el archivo .ipynb en donde se construyó el código, se realizó el análisis y revisión preliminar de los datos. 


# CONCLUSIONES

# Una vez realizado todo el proceso de entendimiento del problema, formulación de la pregunta, transformación y prueba de los datos, se procedió a realizar el análisis exploratorio preliminar de los datos. Teniendo esto, se realizó el cálculo de la regresión lineal (XGBoost, Catboost y el análisis exploratorio de estos resultados), obtenidos los resultados procedemos a implementar PCA con las bases de datos obtenidas, se realizan análisis con variables categoricas (tipo dummie) y sin estas, se realizan pruebas en donde podemos concluir que estas variables no aportan al modelo, por tal razón las omitimos y procedemos a correr el modelo y dar solución a la respuesta planteada previamente, en líneas generales podemos concluir que: 
•	El manejo los parámetros e hiperparámetros de los diversos modelos no tiene una manera comprobada que nos indique como debemos incluirlos para obtener buenos resultados, la implementación de buenos hiperparámetros se consigue con la experimentación, conocimiento y entendimiento de los datos del negocio o problema.   
•	Es importante considerar la cantidad de datos a procesar, ya que esto influye directamente en el costo computacional de los algoritmos utilizados. Por lo tanto, es necesario equilibrar el costo computacional con el rendimiento y la precisión del modelo, de manera que se puedan obtener resultados rápidos, confiables y que conduzcan a una solución coherente. 
•	Las mayores ventajas que brinda el aprendizaje no supervisado, es la facilitación del agrupamiento de los datos, este fue parte fundamental para dar solución a la pregunta que planteada para el desarrollo del proyecto. 
•	Al realizar proyectos de análisis de datos, es recomendable abordar la solución desde diversas perspectivas para corroborar resultados y seleccionar la opción más eficiente en términos de recursos. Además, la solución o el enfoque inicial pueden cambiar a medida que avanza el proyecto, ya que es común enfrentarse a desafíos como la calidad de los datos, la correcta aplicación de los modelos, el costo computacional y la interpretabilidad de los resultados, entre otros factores.
•	Para realizar futuros análisis se sugiere utilizar una muestra de información más amplia, incluyendo información geográfica y niños con diferentes diagnósticos, no necesariamente desnutrición.
•	Al concluir el ejercicio, se observa que el clustering con K-medias tiene el mejor desempeño, se logran observar tres grupos: uno con mejores características físicas actuales y buena alimentación, pero con condiciones al nacer estándar; otro con condiciones estándar al nacer, pero menor desarrollo corporal y condiciones alimentarias; y un tercero más disperso, con bajas condiciones al nacer y un amplio espectro de desarrollo físico y condiciones alimentarias, desde rangos deficientes hasta condiciones un poco más allá del estándar.


