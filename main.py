import secrets
from tkinter import *
from tkinter.font import Font
import ttkbootstrap as ttk
import string

def get_pass():
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    
    token1 = ''.join([secrets.choice(alfabeto) for i in range(60)])
    input_generator['state'] = 'normal'
    input_generator.delete("1.0", END)
    input_generator.insert(END, token1)
    input_generator['state'] = 'disabled'
        
window = ttk.Window(themename='darkly')
window.title("Password generator")
window.geometry("800x400")

first_container = ttk.Frame(window)
first_container.pack(pady=10)

second_container = ttk.Frame(window)
second_container.pack(pady=20)

third_container = ttk.Frame(window)
third_container.pack(pady=20)

title_label = ttk.Label(first_container, text="Generator of passwords", font= 'Calibri 32 bold')
title_label.pack()

input_generator = ttk.Text(second_container, width=40, height=2, state='disabled')
fonte = Font(size=20)
input_generator.configure(font=fonte)
input_generator.pack(side=LEFT)

butto_generate = ttk.Button(third_container, text="Generate password", command=get_pass, width=40)
butto_generate.pack()
window.mainloop()