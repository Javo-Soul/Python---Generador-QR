import pyqrcode
import png
from tkinter import *
from tkinter import messagebox
import os

directorio = os.path.abspath(os.getcwd())

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("500x400")
mywindow.title("Generador QR")
mywindow.resizable(False,False)
mywindow.config(background = "ghost white")
main_title = Label(text = "Generador de QR", font = ("Cambria", 14), bg = "blue2", fg = "white", width = "500", height = "2")
main_title.pack()

link_label = Label(text = "LINK", bg = "#FFEEDD")
link_label.place(x = 22, y = 70)

link = StringVar()
link.set("Ej : https://www.youtube.com/")

link_entry = Entry(textvariable = link, width = "40")
link_entry.place(x = 22, y = 100)
################################################

img_label = Label(text = "Nombre de Foto QR", bg = "#FFEEDD")
img_label.place(x = 22, y = 130)

img = StringVar()
img.set("QR youtube")

img_entry = Entry(textvariable = img, width = "40")
img_entry.place(x = 22, y = 150)

made_label = Label(text = "Hecho por Javier Carrion", bg = "#FFEEDD")
made_label.place(x = 320, y = 350)

def genera_qr():
      link_info = link.get()
      img_info = img.get()
      foto = img_info+'.png'
      try:
        qr_code = pyqrcode.create(link_info)
        qr_code.png(foto, scale=5)
        messagebox.showinfo(message="Se Guardo Imagen QR :"+directorio, title="Listo")
      except Exception as e:
        messagebox.showinfo(message="Error", title="Error")
        print("Ocurrió un error al insertar: ", e)

########################################################## Botones de Comando ##########################################################
# Ejecuta datos con info de clientes
submit_btn_search = Button(mywindow,text = "Generar QR", width = "17", height = "2", command = genera_qr, bg = "#00CD63")
submit_btn_search.place(x = 22, y = 300)

mywindow.mainloop()




