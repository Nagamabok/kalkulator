from tkinter import *
import tkinter.font as font
import math
root = Tk()
root.title('kalkuator')
root['bg']= '#d1d1d1'
root.geometry("310x400")
my_font = font.Font(size = 15)
e = Entry(root, width= 25, borderwidth= 0)
e['font'] = my_font
e['bg']= '#d1d1d1'
e.grid(row= 0, columnspan= 4, pady= 20, padx= 20)
def cetak(nilai):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nilai))
def tambah():
    n0 = e.get()
    global n_0
    global mtk
    mtk = 'penjumlahan'
    n_0 = int(n0)
    e.delete(0, END)
def kurang():
    n0 = e.get()
    global n_0
    global mtk
    mtk = 'pengurangan'
    n_0 = int(n0)
    e.delete(0, END)
def bagi():
    n0 = e.get()
    global n_0
    global mtk
    mtk = 'pembagian'
    n_0 = int(n0)
    e.delete(0, END)
def kali():
    n0 = e.get()
    global n_0
    global mtk
    mtk = 'perkalian'
    n_0 = int(n0)
    e.delete(0, END)
def hapus():
    e.delete(0,END)
def sama_dengan():
    n1 = e.get()
    e.delete(0, END)
    if mtk == 'penjumlahan':
        e.insert(0, n_0 + int(n1))
    elif mtk == 'pengurangan':
        e.insert(0, n_0 - int(n1))
    elif mtk == 'perkalian':
        e.insert(0, n_0 * int(n1))
    elif mtk == 'pembagian':
        e.insert(0, n_0 / int(n1))
button_0 = Button(root, text= '0', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(0))
button_1 = Button(root, text= '1', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(1))
button_2 = Button(root, text= '2', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(2))
button_3 = Button(root, text= '3', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(3))
button_4 = Button(root, text= '4', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(4))
button_5 = Button(root, text= '5', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(5))
button_6 = Button(root, text= '6', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(6))
button_7 = Button(root, text= '7', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(7))
button_8 = Button(root, text= '8', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(8))
button_9 = Button(root, text= '9', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= lambda:cetak(9))

button_plus = Button(root, text= '+', padx= 30, bg= '#878787', fg= 'white',pady= 20, command= tambah)
button_min = Button(root, text= '-', padx= 30, bg= '#878787', fg= 'white',pady= 20, command= kurang)
button_x = Button(root, text= 'x', padx= 30, bg= '#878787', fg= 'white',pady= 20, command= kali)
button_dvd = Button(root, text= '/', padx= 30, bg= '#878787', fg= 'white',pady= 20, command= bagi)

button_eq = Button(root, text= '=', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= sama_dengan)
button_AC = Button(root, text= 'AC', padx= 30, bg= '#3d3d3d', fg= 'white',pady= 20, command= hapus)

button_0.grid(row= 4, column= 1, pady= 2)
button_1.grid(row= 3, column= 0, pady= 2)
button_2.grid(row= 3, column= 1, pady= 2)
button_3.grid(row= 3, column= 2, pady= 2)
button_4.grid(row= 2, column= 0, pady= 2)
button_5.grid(row= 2, column= 1, pady= 2)
button_6.grid(row= 2, column= 2, pady= 2)
button_7.grid(row= 1, column= 0, pady= 2)
button_8.grid(row= 1, column= 1, pady= 2)
button_9.grid(row= 1, column= 2, pady= 2)

button_plus.grid(row= 1, column= 3, pady= 2)
button_min.grid(row= 2, column= 3, pady= 2)
button_x.grid(row= 3, column= 3, pady= 2)
button_dvd.grid(row= 4, column= 3, pady= 2)
button_eq.grid(row= 5, column= 3, pady= 2)
button_AC.grid(row= 6, column= 3, pady= 2)

root.mainloop()