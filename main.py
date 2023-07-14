from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if input_website.get() != "" and input_email.get() != "" and input_password.get() != "":
        messagebox.askokcancel(title="Save Password", message="Are you sure you want to save your password?")
        with open("data.txt", mode="a") as data:
            data.write(f"{input_website.get()} | {input_email.get()} | {input_password.get()}\n")
    else:
        messagebox.showerror(title="Save Password", message="Please fill in all the fields")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#labels
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0, sticky = E)

label_email = Label(text="Email/Username: ")
label_email.grid(row=2, column=0, sticky = E)

label_password = Label(text="Password: ")
label_password.grid(row=3, column=0, sticky= E)

#inputs
input_website = Entry(width=52)
input_website.grid(row=1, column=1, sticky = W, columnspan=2)
input_website.focus()

input_email = Entry(width=52)
input_email.grid(row=2, column=1, sticky = W, columnspan=2)

input_password = Entry(width=32)
input_password.grid(row=3, column=1, sticky = W)

#buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2, sticky= W)

button_add = Button(text="Add", width=43, command=save_data)
button_add.grid(row=4, column=1, columnspan=2, pady=15, )

window.mainloop()
