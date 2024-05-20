from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
# FUNCTION FOR SEARCH BUTTON AND IMPLEMENTING EXCEPTIONS BECAUSE WHEN WE FIRST RUN PROGRAM JSON FILES NOT EXIST!!!
def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# FUNCTION FOR THE GENERATE PASSWORD BUTTON
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    generated_password_list = password_letters + password_symbols + password_numbers
    random.shuffle(generated_password_list)
    generated_password = ''.join(generated_password_list)
    # INSERT FUNCTION WRITES IN THE PASSWORD ENTRY AS SOON AS IS GENERATED
    password_input.insert(0, generated_password)
    # WE INSTALLED PYPERCLIP AND WITH THIS COMMAND THE GENERATED PASSWORD COPIED TO CLIPBOARD AND READY TO USE
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


# CREATING A FUNCTION FOR THE ADD BUTTON WHERE WE GET INPUTS FROM THE ENTRIES
# WE WRITE INTO THE FILE
# THEN AFTER ADD BUTTON PRESSED DELETES EVERYTHING AND START THE CURSOR FROM THE FIRST ENTRY
def save_data():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:
        {"email": email,
         "password": password,
         }
    }
    # IF USER LEAVES BLANK THE ENTRIES THEN WE POP UP A MESSAGE WINDOW
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please no fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                # READING OLD DATA
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # UPDATING OLD DATA WITH NEW DATA
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # SAVING UPDATED DATA
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, 'end')
            password_input.delete(0, 'end')
            web_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

# CREATING THE WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CREATING THE CANVAS AND IMPORTING THE IMAGE
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# CREATING THE LABELS
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# CREATING INPUT PROMPTS

web_input = Entry(width=21)
web_input.grid(column=1, row=1, sticky="EW")
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "niqos@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# CREATING BUTTONS

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
