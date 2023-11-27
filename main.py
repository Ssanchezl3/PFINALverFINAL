# main.py
import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from analisis import mostrar_emojis, mostrar_resultados

# Función que se ejecutará al hacer clic en el botón
def mostrar_mensaje():
    mensaje = cuadro_texto.get()
    etiqueta_salida.config(text="" + mensaje)

    mostrar_resultados(mensaje, etiqueta_salida, canvas, directorio_emoji)


# Función para cargar imágenes desde un directorio
def cargar_imagenes(directorio):
    imagenes = []
    for filename in os.listdir(directorio):
        if filename.endswith(".png"):
            path = os.path.join(directorio, filename)
            imagen = Image.open(path)
            imagen = imagen.resize((50, 50))  # Ajusta el tamaño según sea necesario
            imagen = ImageTk.PhotoImage(imagen)
            imagenes.append(imagen)
    return imagenes



# Directorio donde se encuentran las imágenes de emoji
# Directorio donde se encuentran las imágenes de emoji
directorio_emoji = os.path.join("C:/", "Users", "Santiago", "Downloads", "png", "png")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Prfinal")

# Cargar las imágenes desde el directorio
imagenes_emoji = cargar_imagenes(directorio_emoji)

# Cargar la imagen PNG y redimensionarla (cambiar los valores de los argumentos según sea necesario)
imagen_logo = PhotoImage(file='C:\\Users\\Santiago\\Downloads\\logo_eafit_completo.png').subsample(2, 2)

# Crear un widget Label para mostrar la imagen
label_logo = tk.Label(ventana, image=imagen_logo)
label_logo.grid(row=0, column=0, rowspan=6, padx=2, pady=2, sticky=tk.W)  # Alineado a la izquierda

# Crear un título al lado de la imagen
titulo_programa = tk.Label(ventana, text="UNIVERSIDAD EAFIT PROYECTO FINAL \n LENGUAJES DE PROGRAMACION",
                           font=("Helvetica", 16, "bold"))
titulo_programa.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NW)  # Alineado en la esquina superior derecha

# Crear un título al lado de la caja de entrada
titulo_ingresar_texto = tk.Label(ventana, text="Ingresar Texto:", font=("Helvetica", 12))
titulo_ingresar_texto.grid(row=1, column=1, padx=2, pady=2, sticky=tk.E)  # Alineado a la derecha

# Crear un cuadro de entrada
cuadro_texto = tk.Entry(ventana)
cuadro_texto.grid(row=1, column=2, padx=2, pady=2, sticky=tk.W)  # Alineado a la izquierda

# Crear un botón
boton = tk.Button(ventana, text="TRADUCIR", command=mostrar_mensaje)
boton.grid(row=2, column=1, columnspan=2, pady=2)  # Columnspan para que ocupe dos columnas

# Crear una etiqueta para mostrar el mensaje
etiqueta = tk.Label(ventana, text="", justify=tk.CENTER)
etiqueta.grid(row=3, column=0, columnspan=2, pady=2)  # Columnspan para que ocupe dos columnas

# Crear un título de salida
titulo_salida = tk.Label(ventana, text="SALIDA:", font=("Helvetica", 12))
titulo_salida.grid(row=4, column=1, padx=2, pady=2, sticky=tk.NW)  # Alineado en la esquina superior derecha

# Crear una etiqueta para mostrar la salida
etiqueta_salida = tk.Label(ventana, text="", justify=tk.CENTER)
etiqueta_salida.grid(row=5, column=0, columnspan=2, pady=2, sticky=tk.W)  # Centered with respect to two columns

# Crear un Canvas para mostrar las imágenes de emojis
canvas = tk.Canvas(ventana, width=200, height=60)
canvas.grid(row=4, column=2, padx=2, pady=2, sticky=tk.W)  # Adjust padx to place to the right of etiqueta_salida

# Iniciar el bucle de eventos
ventana.mainloop()

