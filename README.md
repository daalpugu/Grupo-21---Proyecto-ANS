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



# El desarrollo del proyecto se encuentra en su primera fase, exploratoria; teniendo estos resultados se procederá a verificar la utilización de los modelos de aprendizaje no supervisado para lograr responder a la pregunta que está planteada en el inicio del README. 

