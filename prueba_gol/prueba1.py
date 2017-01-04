from tkinter import *
import time
global x
global y
ventana =Tk()
ventana.title("Prueba")

canvas1 = Canvas(ventana,width=900,height=200)
canvas1.pack()
imagen1=PhotoImage(file="arco.png")
canvas1.create_image(0,0,anchor=NW,image=imagen1)

canvas = Canvas(ventana,width=400,height=400)
canvas.pack()
imagen = PhotoImage(file="balon.gif")
canvas.create_image(0,0,anchor=NW,image=imagen)

def mover_imagen(event):
    global conx
    global cony
    if event.keysym == 'Up':
         canvas.move(1,0,-3)
         cony=cony+3
         print(cony)
    elif event.keysym =='Left':
        canvas.move(1,-3,0)
        conx=conx-3
        print(conx)
    else:
         canvas.move(1,3,0)
         conx=conx+3
         print(conx)
    print("Posicion: ",x,y)
    
def mensaje():
    
    ventana1 = Tk()
    ventana1.title("Gol")
    ventana1.geometry("100x100")
    ventana1.configure(background="black")
    mensaje = "Gol"
    msg = Message(ventana1, text = mensaje)
    msg.config(bg='black',fg ="white",font=('times', 20, 'italic'))
    msg.pack( )
    


canvas.bind_all('<KeyPress-Up>',mover_imagen)
canvas.bind_all('<KeyPress-Down>',mover_imagen)
canvas.bind_all('<KeyPress-Left>',mover_imagen)
canvas.bind_all('<KeyPress-Right>',mover_imagen)
ventana.mainloop()
if imagen(0,0,0)>imagen1(20,20):
    mensaje()
    


    
