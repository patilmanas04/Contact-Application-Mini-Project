import tkinter as tk
from tkinter import messagebox

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    
    if name.strip() == "" or email.strip() == "" or phone_number.strip() == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        phone_number = int(phone_number)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return
    
    add_contact(name, email, phone_number)
    messagebox.showinfo("Success", "Contact added successfully.")

# Function to search for contacts
def search_contact():
    search_term = search_entry.get()
    searched_contacts = search_contact(search_term)
    # display_searched_contacts(searched_contacts)

# Function to open contact details
def open_contact_details():
    contact_name = contact_name_entry.get()
    if not contact_name.strip():
        messagebox.showerror("Error", "Please enter a contact name.")
        return
    
    # try:
        # contact = open_contact(contact_name)
        # contact_details_label.config(text=f"Name: {contact['name']}\nEmail: {contact['email']}\nPhone Number: {contact['phone_number']}")
    # except IndexError:
    #     messagebox.showerror("Error", "Contact not found.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Phonebook Application")

# Create and pack the frames
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

open_frame = tk.Frame(root)
open_frame.pack(pady=10)

# Add Contact Frame
name_label = tk.Label(add_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1, padx=5)

email_label = tk.Label(add_frame, text="Email:")
email_label.grid(row=0, column=2, padx=5)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=0, column=3, padx=5)

phone_label = tk.Label(add_frame, text="Phone Number:")
phone_label.grid(row=0, column=4, padx=5)
phone_entry = tk.Entry(add_frame)
phone_entry.grid(row=0, column=5, padx=5)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=6, padx=5)

# Search Contact Frame
search_label = tk.Label(search_frame, text="Search Term:")
search_label.grid(row=0, column=0, padx=5)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_contact)
search_button.grid(row=0, column=2, padx=5)

# Open Contact Frame
contact_name_label = tk.Label(open_frame, text="Contact Name:")
contact_name_label.grid(row=0, column=0, padx=5)
contact_name_entry = tk.Entry(open_frame)
contact_name_entry.grid(row=0, column=1, padx=5)

open_button = tk.Button(open_frame, text="Open Contact Details", command=open_contact_details)
open_button.grid(row=0, column=2, padx=5)

contact_details_label = tk.Label(open_frame, text="")
contact_details_label.grid(row=1, columnspan=3, padx=5)

root.mainloop()