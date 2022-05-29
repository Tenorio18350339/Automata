# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cgitb import text
from tkinter import *

"""Clase para limpiar los valores"""
def clean():
    lista.clear()
    nueva.clear()
    N1val=StringVar()
    res.config(text="")
    txt.delete("0","end")


"""Clase para el automata, aqui se hace el analizis de la cadena"""
def go ():
    val=True
    n2=(N1val.get())
    for i in n2:
        lista.append(i)
    print(lista)
    if(lista[0]!="1"):
        print("Debe iniciar con un 1")
        val=False
    else:
        if(lista[1]!="0"):
            print("Debe seguir con un 0")
            val=False
        else:
            if(lista[2]!="1"):
                print("Debe continuar con un 1")
                val=False
            else:
                if(len(lista)>3):
                    lista.pop(0)
                    lista.pop(1)
                    """lista.pop(2)"""
                    for i in lista:
                        nueva.append(i)
                    for i in nueva:
                        print(nueva)
                        if(i=="0"):
                            print(i)
                            val=True
                        else:
                            val=False
                else:
                    val=False
    if(val==True):
        print("Tu cadena es correcta")
        res.config(text="Cadena Valida")
    else:
        print("No esta bien tu cadena")
        res.config(text="Cadena Invalida")
                
"""Es la parte del diseño de la interfaz y todos los componentes"""                
root=Tk()
frame = Frame()
frame = Frame(root,width=500,height=120,bg= "coral")
frame.pack(side="top", anchor="e")
frame.pack(fill = "y" , expand = 1)
frame.pack(fill = "both", expand = 1)
lista=[]
nueva=[]
N1val=StringVar()
root.iconbitmap('b.ico')

frame2 = Frame(root, bg= "cyan")
frame2.pack(side="top", anchor="e")
frame2.pack(fill = "y" , expand = 1)
frame2.pack(fill = "both", expand = 1)
root.title("Automata")
root.config()
inst=Label(frame2,text="Ingresa el valor que deseas que sea validado").pack()
txt=Entry(frame2, justify=CENTER, textvariable=N1val)
txt.pack()
btn1=Button(frame2,text="Validar", command=go, bg= "cyan").pack()
btn1=Button(frame2,text="Limpiar", command=clean, bg= "coral").pack()

frame = Frame(root,width=500,height=120,bg= "coral")
frame.pack(side="top", anchor="e")
frame.pack(fill = "y" , expand = 1)
frame.pack(fill = "both", expand = 1)
res=Label(root)
res.pack()


root.mainloop()