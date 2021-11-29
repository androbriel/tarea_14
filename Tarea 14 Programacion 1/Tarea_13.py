
#Agregando información para un primer cambio!!


import pyodbc
import pandas as pd
import tkinter as tk

from tkinter import *
from tkinter import ttk #Importamos todas las funciones que contiene tkinter
from tkinter.ttk import *
from tkinter import messagebox

class General:
	def __init__(self, raiz):
		self.cliente = StringVar()
		self.label_cliente = Label(raiz, text = "Cliente")
		self.label_cliente.grid(column=0, row=0)
		self.cliente = Combobox(raiz, values=('Miguel', 'Sergio','Federico','Erick'), width=5)
		self.cliente.grid(column=0, row=1)

		self.unidades = StringVar()
		self.label_unidades = Label(raiz, text = "Unidades_compradas")
		self.label_unidades.grid(column=0, row=5)
		self.unidades = Spinbox(raiz, values=("5", "7", "20", "30", "2"), width=10)
		self.unidades.grid(column=0,row=6)

		#Creamos los botones
		#Con command le decimos cual función queremos que lleve a cabo
		self.boton_buscar= Button(raiz, text="Buscar", command=self.buscar)
		self.boton_buscar.grid(column=0, row=20)

		self.boton_borrar=Button(raiz, text="Borrar", command=self.borrar)
		self.boton_borrar.grid(column=0, row=30)

	def buscar(self):
		server = 'LAPTOP-M49SUP7Q\SQLEXPRESS'
		bd = 'DB_Tarea'
		cliente_valor = "'" + self.cliente.get() + "'"
		print(cliente_valor)

		unidades_valor = "'" + self.unidades.get() + "'"
		print(unidades_valor)

		try:
				conexion = pyodbc.connect(driver='{SQL server}', host = server, database = bd)
				print('Conexión exitosa')
		except:
				print('La conexión no fué exitosa')

		#Creamos un cursor para almacenar la información en memoria
		cursor = conexion.cursor()

		cursor.execute("SELECT * FROM Tarea_pedidos WHERE Cliente = " + cliente_valor + " AND Unidades_compradas =" + unidades_valor)

		datos_clientes = cursor.fetchall()
		print(datos_clientes)
		conexion.commit()


		#Nos aseguramos de cerrar la conexión
		conexion.close()

		messagebox.showinfo("Resultados", datos_clientes)

	#def desplegar_resultados(self):

	def borrar(self):
		self.genero.set("")
		self.estado.set("")


#Creamos el objeto que será la raiz de la aplicación
raiz = Tk()
#Le agregamos un título
raiz.title("Filtrando Información")
#Determinamos si se podrá cambiar su tamaño
raiz.resizable(1,1)
#Asignamos un logotipo
#raiz.iconbitmap('objetos.ico')
#Asignamos un tipo de cursor, un color de background y un borde a la raiz
raiz.config(bd=8)
raiz.config(relief="ridge")
estructura = General(raiz)

raiz.mainloop()