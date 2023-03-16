from tkinter import messagebox
import tkinter as tk
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():
    password_entry.delete(0, tk.END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for num1 in range(nr_letters)]

    [password_list.append(random.choice(numbers)) for num2 in range(nr_symbols)]

    [password_list.append(random.choice(symbols)) for num3 in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(tk.END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website.get()
    email = email_entry.get()
    my_password = password_entry.get()
    new_data = {
        web: {
            "Email": email,
            "Password": my_password
        }
    }

    if len(web) == 0 or len(email) == 0 or len(my_password) == 0 \
            or " " in web or " " in email or " " in my_password:
        messagebox.showinfo(title="Oops", message="Please dont leave any of the fields empty.")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        except ValueError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(title="Processed", message="The file was saved successfully")
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Processed", message="The file was saved successfully")
        finally:
                website.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                website.focus()


#---------------------------RESET PASSWORD -------------------------#

#---------------------------- FIND PASSWORD ---------------------------#
def find_password():
    web = website.get()
    my_password = password_entry.get()
    email = email_entry.get()
    with open("data.json", "r") as file:
        try:
            data = json.load(file)
            the_password = data[web]["Password"]
            if web in data:
               modify =  messagebox.showinfo(title=web, message=f"Email:{email}\nPassword:{the_password}")
        except KeyError:
            messagebox.showinfo(title="Oops", message="No details for the website exists")
        except ValueError:
            messagebox.showinfo(title="Error", message="No Data File Found\nPlease add an item to the file.")
        else:
            pass
        finally:
                website.delete(0, tk.END)
                password_entry.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #



window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

website = tk.Entry(width=33)
website.focus()
website.grid(row=2, column=2)
website_label = tk.Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(row=2, column=1)

email_entry = tk.Entry(width=50)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "abayo172000@gmail.com")
email_label = tk.Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=1, row=3)

search_button = tk.Button(text="Search", width=13,command=find_password)
search_button.grid(column=3, row=2)

password_entry = tk.Entry(width=33)
password_entry.grid(row=4, column=2)
password_label = tk.Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=1, row=4)

generate_password = tk.Button(text="Generate Password", command=gen_password, width=14)
generate_password.grid(row=4, column=3)

add_button = tk.Button(text="Add", width=42, command=save_data)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
