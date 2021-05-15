from os import *
from tkinter import *

w = Tk()
def start():
    w.title('Задание')
    w.geometry('400x1140')
    task()
    task_check()
    return mainloop()

def open_photoshop():
    #Путь к программе
    startfile(r"Запуск программы")

def task1():
    startfile('Открытие файлв')
def task1_1():
    startfile('Открытие файлв')
def task1_2():
    startfile('Открытие файлв')
def task2():
    startfile('Открытие файлв')
def task2_1():
    startfile('Открытие файлв')
def task3():
    startfile('Открытие файлв')
def task3_1():
    startfile('Открытие файлв')
def task4():
    startfile('Открытие файлв')
def task5():
    startfile('Открытие файлв')

def task():
    t1=Label(w, text='Практическая 2',font=('Arial Bord',20))
    t1.grid(column=0, row=0)
    t1_1 = Label(w, text='Практическая 2.1', font=('Arial Bord', 20))
    t1_1.grid(column=0, row=1)
    t1_2 = Label(w, text='Практическая 2.2', font=('Arial Bord', 20))
    t1_2.grid(column=0, row=2)
    t2=Label(w, text='Практическая 3',font=('Arial Bord',20))
    t2.grid(column=0, row=3)
    t2_1 = Label(w, text='Практическая 3.1', font=('Arial Bord', 20))
    t2_1.grid(column=0, row=4)
    t3=Label(w, text='Практическая 4',font=('Arial Bord',20))
    t3.grid(column=0, row=5)
    t3_1 = Label(w, text='Практическая 4.1', font=('Arial Bord', 20))
    t3_1.grid(column=0, row=6)
    t4=Label(w, text='Практическая 5',font=('Arial Bord',20))
    t4.grid(column=0, row=7)
    t5=Label(w, text='Практическая 7',font=('Arial Bord',20))
    t5.grid(column=0, row=8)
    t5_1 = Label(w, text='Практическая 7.1', font=('Arial Bord', 20))
    t5_1.grid(column=0, row=9)
    t5_2 = Label(w, text='Практическая 7.2', font=('Arial Bord', 20))
    t5_2.grid(column=0, row=10)
    t5_3 = Label(w, text='Практическая 7.3', font=('Arial Bord', 20))
    t5_3.grid(column=0, row=11)
    t6=Label(w, text='Практическая 8',font=('Arial Bord',20))
    t6.grid(column=0, row=12)
    t6_1 = Label(w, text='Практическая 8.1', font=('Arial Bord', 20))
    t6_1.grid(column=0, row=13)
    t7=Label(w, text='Практическая 9',font=('Arial Bord',20))
    t7.grid(column=0, row=14)
    t8=Label(w, text='Практическая 10',font=('Arial Bord',20))
    t8.grid(column=0, row=15)
    t9=Label(w, text='Практическая 11',font=('Arial Bord',20))
    t9.grid(column=0, row=16)
    t10=Label(w, text='Практическая 12',font=('Arial Bord',20))
    t10.grid(column=0, row=17)
    t11=Label(w, text='Практическая 13',font=('Arial Bord',20))
    t11.grid(column=0, row=18)
    t12=Label(w, text='Практическая 14',font=('Arial Bord',20))
    t12.grid(column=0, row=19)
    t13=Label(w, text='Практическая 15',font=('Arial Bord',20))
    t13.grid(column=0, row=20)
    t14=Label(w, text='Практическая 15.1',font=('Arial Bord',20))
    t14.grid(column=0, row=21)
    t14 = Label(w, text='Практическая 16', font=('Arial Bord', 20))
    t14.grid(column=0, row=22)
    t15=Label(w, text='Практическая 17',font=('Arial Bord',20))
    t15.grid(column=0, row=23)
def task_check():
    #Написать путь к папки с файлами
    task_place='Папка'
    list=listdir(task_place)
    #Написать название и расширение файла
    if 'Файл' in list:
        b1 = Button(w, text='Выполнено', font=('Arial Bord', 16),fg="green",command=task1)
        b1.grid(column=2, row=0)
    else:
        b1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b1.grid(column=2, row=0)
    if 'Файл' in list:
        b1_1 = Button(w, text='Выполнено', font=('Arial Bord', 16),fg="green",command=task1_1)
        b1_1.grid(column=2, row=1)
    else:
        b1_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b1_1.grid(column=2, row=1)
    if 'Файл' in list:
        b1_2 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task1_2)
        b1_2.grid(column=2, row=2)
    else:
        b1_2 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b1_2.grid(column=2, row=2)
    if 'Файл' in list:
        b3 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task2)
        b3.grid(column=2, row=3)
    else:
        b3 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b3.grid(column=2, row=3)
    if 'Файл' in list:
        b3_1 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task2_1)
        b3_1.grid(column=2, row=4)
    else:
        b3_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b3_1.grid(column=2, row=4)
    if 'Файл' in list:
        b4 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task3)
        b4.grid(column=2, row=5)
    else:
        b4 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b4.grid(column=2, row=5)
    if 'Файл' in list:
        b4_1 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task3_1)
        b4_1.grid(column=2, row=6)
    else:
        b4_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b4_1.grid(column=2, row=6)
    if 'Файл' in list:
        b5 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task4)
        b5.grid(column=2, row=7)
    else:
        b5 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red",command=open_photoshop)
        b5.grid(column=2, row=7)
    if 'Файл' in list:
        b6 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green",command=task5)
        b6.grid(column=2, row=8)
    else:
        b6 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b6.grid(column=2, row=8)
    if 'Файл' in list:
        b6_1 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green", command=open_photoshop)
        b6_1.grid(column=2, row=9)
    else:
        b6_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b6_1.grid(column=2, row=9)
    if 'Файл' in list:
        b6_2 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green", command=open_photoshop)
        b6_2.grid(column=2, row=10)
    else:
        b6_2 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b6_2.grid(column=2, row=10)
    if 'Файл' in list:
        b6_3 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b6_3.grid(column=2, row=11)
    else:
        b6_3 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b6_3.grid(column=2, row=11)
    if 'Файл' in list:
        b7 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green", command=open_photoshop)
        b7.grid(column=2, row=12)
    else:
        b7 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b7.grid(column=2, row=12)
    if 'Файл' in list:
        b7_1 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green", command=open_photoshop)
        b7_1.grid(column=2, row=13)
    else:
        b7_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b7_1.grid(column=2, row=13)
    if 'Файл' in list:
        b8 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b8.grid(column=2, row=14)
    else:
        b8 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b8.grid(column=2, row=14)
    if 'Файл' in list:
        b9 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b9.grid(column=2, row=15)
    else:
        b9 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b9.grid(column=2, row=15)
    if 'Файл' in list:
        b10 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b10.grid(column=2, row=16)
    else:
        b10 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b10.grid(column=2, row=16)
    if 'Файл' in list:
        b11 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b11.grid(column=2, row=17)
    else:
        b11 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b11.grid(column=2, row=17)
    if 'Файл' in list:
        b12 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b12.grid(column=2, row=18)
    else:
        b12 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b12.grid(column=2, row=18)
    if 'Файл' in list:
        b13 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b13.grid(column=2, row=19)
    else:
        b13 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b13.grid(column=2, row=19)
    if 'Файл' in list:
        b13 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b13.grid(column=2, row=20)
    else:
        b13 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b13.grid(column=2, row=20)
    if 'Файл' in list:
        b14 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b14.grid(column=2, row=21)
    else:
        b14 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b14.grid(column=2, row=21)
    if 'Файл' in list:
        b14_1 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b14_1.grid(column=2, row=22)
    else:
        b14_1 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b14_1.grid(column=2, row=22)
    if 'Файл' in list:
        b15 = Button(w, text='Выполнено', font=('Arial Bord', 16), fg="green")
        b15.grid(column=2, row=23)
    else:
        b15 = Button(w, text='Не выполнено', font=('Arial Bord', 16), fg="red", command=open_photoshop)
        b15.grid(column=2, row=23)


start()