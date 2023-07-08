import secrets
from tkinter import *
from tkinter.font import Font
import ttkbootstrap as ttk
import string

def main():
    window = ttk.Window(themename='darkly')
    window.title("Password generator")
    window.geometry("800x500")

    first_container = ttk.Frame(window)
    first_container.pack(pady=10)

    second_container = ttk.Frame(window)
    second_container.pack(pady=20)

    second_container_number_of_characters = ttk.Frame(second_container)
    second_container_number_of_characters.pack(side=LEFT, padx=100)

    second_container_checkbuttons = ttk.Frame(second_container)
    second_container_checkbuttons.pack(side=RIGHT, padx=100)

    third_container = ttk.Frame(window)
    third_container.pack(pady=20)

    fourth_container = ttk.Frame(window)
    fourth_container.pack(pady=20)

    title_label = ttk.Label(first_container, text="Generator of passwords", font= 'Calibri 32 bold')
    title_label.pack()

    checkboxes = {
        'letters': ttk.BooleanVar(value=True), 
        'numbers': ttk.BooleanVar(value=True),
        'symbols': ttk.BooleanVar(value=True)
    }
    
    #letters = ttk.BooleanVar(value=True)
    check_letters = ttk.Checkbutton(second_container_checkbuttons, variable=checkboxes['letters'], text="Letters", padding=5)
    check_letters.pack()

    check_numbers = ttk.Checkbutton(second_container_checkbuttons, variable=checkboxes['numbers'], text='Numbers', padding=5)
    check_numbers.pack()

    check_simbols = ttk.Checkbutton(second_container_checkbuttons, variable=checkboxes['symbols'], text='Symbols', padding=5)
    check_simbols.pack()

    number_of_characters = ttk.StringVar()
    label_number_of_characters = ttk.Label(second_container_number_of_characters, text="Choose the number of characters:", padding=10)
    label_number_of_characters.pack()

    input_number_of_characters = ttk.Entry(second_container_number_of_characters, textvariable=number_of_characters)
    input_number_of_characters.pack()

    font = Font(size=20)
    input_generator = ttk.Text(third_container, width=40, height=2, state='disabled', font=font)
    input_generator.pack(side=LEFT)
    
    button_generate = ttk.Button(fourth_container, 
                                 text="Generate password", 
                                 command=lambda : get_password(input_generator, number_of_characters, error, checkboxes), 
                                 width=40)
    button_generate.pack()

    error = ttk.StringVar()
    label_error = ttk.Label(window, textvariable=error, foreground='red')
    label_error.pack()
    window.mainloop()

def get_password(input_generator, number_of_characters, error, checkboxes):

    characters = ''
    if checkboxes['letters'].get():
        characters += string.ascii_letters

    if checkboxes['numbers'].get():
        characters += string.digits

    if checkboxes['symbols'].get():
        characters += string.punctuation

    if not characters:
        error.set('You need to choose one or more types of characters')
        input_generator.delete("1.0", END)
        return

    if not number_of_characters.get().isdigit():
        error.set('The quantify needs to be a number')
        return
    
    if error.get:
        error.set('')

    characters_length = int(number_of_characters.get())
    token1 = ''.join([secrets.choice(characters) for _ in range(characters_length)])

    input_generator['state'] = 'normal'
    input_generator.delete("1.0", END)
    input_generator.insert(END, token1)
    input_generator['state'] = 'disabled'

main()