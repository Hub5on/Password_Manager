from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
button_generate = Button(text="Generate Password")
button_generate.grid(row=3, column=2, sticky= W)

button_add = Button(text="Add", width=43, command=save_data)
button_add.grid(row=4, column=1, columnspan=2, pady=15, )

window.mainloop()
