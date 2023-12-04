import math
from tkinter import *
from tkinter import ttk
 
def functionSch(a, b, h, m):
    i=1
    x = a
    while(x<=b):
        result = x**3-m*math.sin(x)
        results.append((i,round(x,3),round(result,3)))
        i+=1
        x+=h

root = Tk()
root.title("LR3")
root.geometry("600x400") 

def funcSchCall():
    functionSch(float(spinboxA.get()), float(spinboxB.get()), float(spinboxH.get()), float(spinboxM.get()))
    for result in results:
        tree.insert("", END, values=result)

label = Label(text="f(x)=x^3+msin(x)") # создаем текстовую метку
label.pack(anchor="nw", padx=20, pady=30)

label = Label(text="Введите начало диапазона a:") # создаем текстовую метку
label.pack()    # размещаем метку в окне
spinboxA = ttk.Spinbox(from_=-100.0, to=100.0, increment=0.1)
spinboxA.pack(anchor=NW)

label = Label(text="Введите начало диапазона b: ") # создаем текстовую метку
label.pack()    # размещаем метку в окне
spinboxB = ttk.Spinbox(from_=-100.0, to=100.0, increment=0.1)
spinboxB.pack(anchor=NW)

label = Label(text="Введите шаг h: ") # создаем текстовую метку
label.pack()    # размещаем метку в окне
spinboxH = ttk.Spinbox(from_=-100.0, to=100.0, increment=0.1)
spinboxH.pack(anchor=NW)

label = Label(text="Введите параметр m:") # создаем текстовую метку
label.pack()    # размещаем метку в окне
spinboxM = ttk.Spinbox(from_=-100.0, to=100.0, increment=0.1)
spinboxM.pack(anchor=NW)

btn = ttk.Button(text="Вычислить", command=funcSchCall)
btn.pack(anchor="nw", padx=20, pady=30)

# определяем столбцы
columns = ("number", "x", "fx")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
tree.heading("number", text="№")
tree.heading("x", text="x")
tree.heading("fx", text="f(x)")

results = []

root.mainloop()