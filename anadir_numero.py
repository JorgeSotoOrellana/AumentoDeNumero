from tkinter import *

root = Tk()
root.title("Test")
root.geometry("500x225")
root.config(bg="black")

lbl = Label(root,
               bg="black",
               fg="white",
               text="numero:")
lbl.pack()

num = StringVar(root, "1")
num_in = Entry(root,
               bg="black",
               fg="white",
               relief= "ridge",
               textvariable=num)


lbl1 = Label(root,
             bg="black",
             fg="white",
             textvariable=num
             )
lbl1.pack()

def incr():
    num.set(
        str(
            int(num.get()) + 1))
    s = num.get()
    
    if s == str(24):
        butt.config(state=DISABLED)
    else:
        butt1.config(state=NORMAL)

def decre():
    num.set(
        str(
            int(num.get()) - 1))
    s = num.get()
    if s == str(0):
        butt1.config(state=DISABLED)
    else:
        butt.config(state=NORMAL)

butt = Button(root,
              bg="black",
              fg="white",
              command=incr,
              activebackground="green",
              text="aumentar",
              relief= "flat",
              state= NORMAL)
butt.pack()

butt1 = Button(root,
              bg="black",
              fg="white",
              command=decre,
              activebackground="red",
              text="disminuir",
              relief= "flat",
              state= NORMAL)
butt1.pack()


butt2 = Button(root,
              bg="black",
              fg="white",
              command=root.destroy,
              text="Cerrar Ventana",
               relief= "flat",
               state=NORMAL)
butt2.pack()


root.mainloop()