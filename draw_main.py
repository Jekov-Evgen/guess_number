from tkinter import *
from tkinter import ttk
from result_functions import error, right, wrong, defeat
from random import randint


class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        self.rand = randint(0, 10)
        self.count = 0
        self.root.title("Игра угадай число")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()

        ttk.Label(text="Приветствуем в игре Угадай число", font="30").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(text="Ваше число уже загадано, введите догадку", font="30").grid(row=1, column=0, padx=10, pady=10)

        self.guess = ttk.Entry(width=50)
        self.guess.grid(row=3, column=0, padx=10, pady=10)

        ttk.Button(text="Отгадать", width=50, command=self.button_processing).grid(row=4, column=0, padx=10, pady=10)

        ttk.Label(text="У вас 5 попыток на одно число", font="30").grid(row=5, column=0, padx=10, pady=10)
        ttk.Label(text="Числа загадываются от 0 до 10", font="30").grid(row=6, column=0, padx=10, pady=10)

    def run(self):
        self.root.mainloop()

    def button_processing(self):
        try:
            res = int(self.guess.get())
        except ValueError:
            error()
            return 

        self.count += 1

        if res == self.rand:
            right() 
            self.rand = randint(0, 10)
            self.count = 0 
        elif self.count >= 5:
            defeat()
            self.root.destroy() 
        else:
            wrong()