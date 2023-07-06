import secrets
from tkinter import *
from tkinter.font import Font
import string

def get_pass():
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    token1 = ''.join([secrets.choice(alfabeto) for i in range(60)])
    input_generator.delete("1.0", END)
    input_generator.insert(END, token1)
        
window = Tk()
window.title("Password generator")
window.geometry("800x600")

first_container = Frame(window)
first_container.pack()

second_container = Frame(window)
second_container.pack()

input_generator = Text(first_container, width=50, height=5)
fonte = Font(size=20)
input_generator.configure(font=fonte)
input_generator.pack(side=LEFT)

butto_generate = Button(second_container, text="Generate password", command=get_pass)
butto_generate.pack()
window.mainloop()