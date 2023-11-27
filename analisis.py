# analisis.py
import re
import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Directorio donde se encuentran las imágenes de emoji
directorio_emoji = os.path.join("C:/", "Users", "Santiago", "Downloads", "png")

mapeo_emojis = {
    ":)": "001-emoji.png",
    ":(": "009-triste.png",
    ":D": "005-sonriente.png",
    "B)": "002-emoticonos.png",
    ";(": "llorando.png",
    ":P": "lengua.png",
    "xD": "xD.png",
    ":l": "sorprendido.png",
    ":3": "062-perro-2.png",
    # Lista de emojis a traducir
}




def get_emoji_string(emoji):
    # Función auxiliar para obtener la representación en cadena del emoji
    return emoji.group()

def analizar_texto(texto):
    emojis = re.findall(r'(?i::\)|:\(|:D|xD|:3|B\))', texto)
    palabras = re.findall(r'\b\w+\b', texto)
    return emojis, palabras


def limpiar_nombre_archivo(nombre):
    # Reemplazar caracteres no permitidos por guiones bajos
    nombre_limpio = re.sub(r'[\\/:*?"<>|]', '_', nombre)
    # Asegurarse de que no termine con un guion bajo
    return nombre_limpio.rstrip('_')

def mostrar_emojis(emojis, canvas, directorio_emoji,texto):
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.delete("all")
    start_position = 0
    for emoji in emojis:
        if emoji in mapeo_emojis:
            nombre_imagen = mapeo_emojis[emoji]
            path = os.path.join(directorio_emoji, nombre_imagen)
            imagen = Image.open(path)
            imagen = imagen.resize((30, 30))
            imagen = ImageTk.PhotoImage(imagen)

            # Find the position of the emoji in the original text
            start = texto.find(emoji, start_position)
            end = start + len(emoji)

            # Insert the text before the emoji
            texto_label = tk.Label(canvas, text=texto[start_position:start])
            texto_label.pack(side=tk.LEFT)

            # Insert the image
            imagen_label = tk.Label(canvas, image=imagen)
            imagen_label.image = imagen
            imagen_label.pack(side=tk.LEFT)

            # Update the start position for the next iteration
            start_position = end

    # Insert the remaining text after the last emoji
    texto_label = tk.Label(canvas, text=texto[start_position:])
    texto_label.pack(side=tk.LEFT)


def mostrar_resultados(texto, etiqueta_salida, lista_imagenes, directorio_emoji):
    for widget in lista_imagenes.winfo_children():
        widget.destroy()
    emojis, palabras = analizar_texto(texto)
    mensaje_salida = f"Se encontraron {len(emojis)} emojis y {len(palabras)} palabras."
    etiqueta_salida.config(text=mensaje_salida)


    if len(emojis)!=0:
        print("run")
        mostrar_emojis(emojis, lista_imagenes, directorio_emoji,texto)



def cargar_diccionario(directorio):
    diccionario = {}
    for filename in os.listdir(directorio):
        if filename.endswith(".txt"):
            path = os.path.join(directorio, filename)
            with open(path, 'r', encoding='utf-8') as file:
                contenido = file.read()
                diccionario[filename] = contenido
    return diccionario
