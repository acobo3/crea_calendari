from tkinter import *
from tkinter import messagebox

def mensaje():
    print("hola tete")

def popup():
    messagebox.showinfo("Sobre mi", "enlace a LinkedIn: \n www.linkedin.com/--")

root = Tk()
root.config(bd=15)
root.geometry("540x480")
root.title("Programar horari")

lbl = Label(root, text="label de tinker")
#lbl.pack()

btn = Button(root, text='presiona este [Button] para el mensaje', command=mensaje)
#btn.pack()
btn.grid(row= 3, column=3)

# imagen = PhotoImage(file="yt.png")
# foto =Label(root, image=imagen, bd=0)
# foto.grid(row=1,column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="más información", menu=helpmenu)
helpmenu.add_command(label="información del autor", command=popup)
menubar.add_command(label="salir", command=root.destroy)

instrucciones = Label(root, text="Introdueix la URL del video de Youtube: \n")
instrucciones.grid(row=0, column=1)

url = Entry(root)
url.grid(row=1, column=1)

root.mainloop()