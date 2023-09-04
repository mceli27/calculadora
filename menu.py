from tkinter  import *


root = Tk()
root.title("Calculadora")

for i in range(6):
    root.grid_rowconfigure(i,weight=1, uniform="row")
    root.grid_columnconfigure(i,weight=1, uniform="col")

display = Entry(root)
display.grid(row=0,column=0,columnspan=6,sticky=W+E)

i = 0

#Funciones
def añadir_numeros(n):
    global i
    display.insert(i, n)
    i+=1

def añadir_operadores(o):
    global i
    o_length = len(o)
    display.insert(i, o)
    i+=o_length
def limpiar():
    display.delete(0,END)

def borrar():
    display_anterior = display.get()
    if len(display_anterior):
        display_nuevo = display_anterior[:-1]
        limpiar()
        display.insert(0,display_nuevo)
    else:
        limpiar()

def calcular():
    display_state=display.get()
    try:
        cuenta = compile(display_state,'menu.py','eval')
        res = eval(cuenta)
        limpiar()
        display.insert(0,res)
    except:
        limpiar()
        display.insert(0,'Error')




#NUMERIC BUTTONS
Button(root,text="1",command=lambda:añadir_numeros(1)).grid(row=2,column=0,sticky=W+E)
Button(root,text="2",command=lambda:añadir_numeros(2)).grid(row=2,column=1,sticky=W+E)
Button(root,text="3",command=lambda:añadir_numeros(3)).grid(row=2,column=2,sticky=W+E)

Button(root,text="4",command=lambda:añadir_numeros(4)).grid(row=3,column=0,sticky=W+E)
Button(root,text="5",command=lambda:añadir_numeros(5)).grid(row=3,column=1,sticky=W+E)
Button(root,text="6",command=lambda:añadir_numeros(6)).grid(row=3,column=2,sticky=W+E)

Button(root,text="7",command=lambda:añadir_numeros(7)).grid(row=4,column=0,sticky=W+E)
Button(root,text="8",command=lambda:añadir_numeros(8)).grid(row=4,column=1,sticky=W+E)
Button(root,text="9",command=lambda:añadir_numeros(9)).grid(row=4,column=2,sticky=W+E)

#Botones operacionales
Button(root,text="AC",command=lambda:limpiar()).grid(row=5,column=0,sticky=W+E)
Button(root,text="0",command=lambda:añadir_numeros(0)).grid(row=5,column=1,sticky=W+E)
Button(root,text="%",command=lambda:añadir_operadores("%")).grid(row=5,column=2,sticky=W+E)

Button(root,text="+",command=lambda:añadir_operadores("+")).grid(row=2,column=3,sticky=W+E)
Button(root,text="-",command=lambda:añadir_operadores("-")).grid(row=3,column=3,sticky=W+E)
Button(root,text="*",command=lambda:añadir_operadores("*")).grid(row=4,column=3,sticky=W+E)
Button(root,text="/",command=lambda:añadir_operadores("/")).grid(row=5,column=3,sticky=W+E)

#Botones 
Button(root,text="←",command=lambda:borrar()).grid(row=2,column=4,sticky=W+E,columnspan=2)
Button(root,text="exp",command=lambda:añadir_operadores("**")).grid(row=3,column=4,sticky=W+E)
Button(root,text="^2",command=lambda:añadir_operadores("**2")).grid(row=3,column=5,sticky=W+E)
Button(root,text="(",command=lambda:añadir_operadores("(")).grid(row=4,column=4,sticky=W+E)
Button(root,text=")",command=lambda:añadir_operadores(")")).grid(row=4,column=5,sticky=W+E)
Button(root,text="=",command=lambda:calcular()).grid(row=5,column=4,sticky=W+E,columnspan=2)



root.mainloop()