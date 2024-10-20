from tkinter import *

def wrong():
    info = Tk()
    Label(info, text="Вы отгадали неправильно", font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="Еще раз", width=50, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)


def right():
    info = Tk()
    Label(info, text="Вы отгадали правильно, загадано новое число", font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="Еще раз", width=50, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)


def defeat():
    info = Tk()
    Label(info, text="Вы проиграли!!!", font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="Выход", width=50, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)


def error():
    info = Tk()
    Label(info, text="Неверный ввод", font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="Еще раз", width=50, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)