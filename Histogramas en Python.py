#Indicamos el directorio en el que vamos a trabajar
import os
os.chdir("C:/Users/camachal/Documents/Alejandro/Maestría/Primer Semestre/Programacion I/")

#Importamos los paquetes que vamos a necesitar 
import pandas as pd #Contiene funciones que nos ayudan en el análisis de datos
import matplotlib.pyplot as plt #Nota: Fue necesario instalar matplotlib 2 con conda install matplotlib=2
                                #y comentar la linea 4 del archivo _classic_test_patch.mplstyle

#Leemos el archivo a analizar
atletas = pd.read_csv('categorias de corredores.csv', index_col=0) #Con index_col=0 le indicamos que las filas tienen un nombre
atletas.info()

#Vemos las primeras filas del archivo
atletas.head()

#Creamos el histograma de la variable Tiempo
plt.figure(1)
plt.hist(atletas['Tiempo'], 15, color="yellow", ec="black")
plt.title("Histograma Tiempo")

plt.savefig("Histograma.jpg")
#Para conocer la frecuencia de una variable que es categórica
import seaborn as sns
plt.figure(2)
sns.countplot(x=atletas['Velocidad'], palette = 'ocean')
plt.savefig("Velocidades.jpg")
#Si queremos saber las velocidades en hombres y en mujeres     
plt.figure(3)
grafico3 = sns.countplot(x = 'Genero', hue = 'Velocidad', palette = 'hot_r', data = atletas)
grafico3.set(title = 'Velocidades por Género',
       xlabel = 'Género', ylabel = 'Total')
plt.title("Gráfico de Barras Genero")
plt.savefig("Genero.jpg")
plt.show()



