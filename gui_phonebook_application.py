import tkinter as tk
from tkinter import messagebox
import json

contacts = []

with open('contacts_store.json', 'r+') as retrived_contacts_file:
    retrived_contacts = retrived_contacts_file.read()

    if retrived_contacts:
        contacts = json.loads(retrived_contacts)
    else:
        contacts = []

def display_searched_contacts(contacts):
    contact_list.delete(1.0, tk.END)

    contact_list.insert(tk.END, f"Search Results:\n")
    if not contacts:
        contact_list.insert(tk.END, f"No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            contact_list.insert(tk.END, f"{i+1}. {contact['name']}")

# Retriving saved contacts from 'contacts_store.json' file
def load_contacts():
    global contacts
    with open('contacts_store.json', 'r') as retrived_contacts_file:
        retrived_contacts = retrived_contacts_file.read()

        if retrived_contacts:
            contacts = json.loads(retrived_contacts)
        else:
            contacts = []

# Updating 'contacts_store.json' file
def update_contacts_file():
    with open('contacts_store.json', 'w') as contact_file:
        contact_file.write(json.dumps(contacts))

# Function to add a new contact
def add_contact(name, email, phone_number):
    global contacts
    contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number
    }

    for existing_contact in contacts:
        if existing_contact['name'].lower() == name.lower():
            messagebox.showerror("Error", "Contact already exists.")
            return

    contacts.append(contact)

    update_contacts_file()
    display_contacts()
    messagebox.showinfo("Success", "Contact added successfully.")

# Function to search for contacts
def search_contact(search_term):
    searched_contacts = []
    for contact in contacts:
        try:
            if type(int(search_term)) == int:
                if search_term in str(contact['phone_number']):
                    searched_contacts.append(contact)
        except:
            if search_term.lower() in contact['name'].lower():
                searched_contacts.append(contact)

    return searched_contacts

# Function to open contact details
def open_contact(contact_name):
    searched_contacts = search_contact(contact_name)
    if not searched_contacts:
        messagebox.showerror("Error", "Contact not found.")
        return None
    return searched_contacts[0]

# Function to display contacts in the text field
def display_contacts():
    contact_list.delete(1.0, tk.END)
    
    if not contacts:
        contact_list.insert(tk.END, "No contacts found.")
    else:
        print("\nContacts -->")
        for i, contact in enumerate(contacts, start=1):
            contact_list.insert(tk.END, f"{i}. {contact['name']}\n")

# Create the main Tkinter window
root = tk.Tk()
root.title("Contact Management Application")

# Create and pack the frames
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

open_frame = tk.Frame(root)
open_frame.pack(pady=10)

display_frame = tk.Frame(root)
display_frame.pack(pady=10)

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

def add_contact_gui():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    
    if not name.strip() or not email.strip() or not phone_number.strip():
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        phone_number = int(phone_number)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return
    
    add_contact(name, email, phone_number)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact_gui)
add_button.grid(row=0, column=6, padx=5)

# Search Contact Frame
search_label = tk.Label(search_frame, text="Search Term:")
search_label.grid(row=0, column=0, padx=5)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5)

def search_contact_gui():
    search_term = search_entry.get()
    searched_contacts = search_contact(search_term)
    display_searched_contacts(searched_contacts)

search_button = tk.Button(search_frame, text="Search", command=search_contact_gui)
search_button.grid(row=0, column=2, padx=5)

# Open Contact Frame
contact_name_label = tk.Label(open_frame, text="Contact Name:")
contact_name_label.grid(row=0, column=0, padx=5)
contact_name_entry = tk.Entry(open_frame)
contact_name_entry.grid(row=0, column=1, padx=5)

def open_contact_details():
    contact_name = contact_name_entry.get()
    if not contact_name.strip():
        messagebox.showerror("Error", "Please enter a contact name.")
        return
    
    try:
        contact = open_contact(contact_name)
        contact_details_label.config(text=f"Name: {contact['name']}\nEmail: {contact['email']}\nPhone Number: {contact['phone_number']}")
    except IndexError:
        messagebox.showerror("Error", "Contact not found.")

open_button = tk.Button(open_frame, text="Open Contact Details", command=open_contact_details)
open_button.grid(row=0, column=2, padx=5)

contact_details_label = tk.Label(open_frame, text="")
contact_details_label.grid(row=1, columnspan=3, padx=5)

# Display Contacts Frame
contact_list_label = tk.Label(display_frame, text="Contacts:")
contact_list_label.pack()

contact_list = tk.Text(display_frame, height=10, width=50, cursor="arrow")
contact_list.pack()

# Display Contacts Button
display_contacts_button = tk.Button(display_frame, text="Display Contacts", command=display_contacts)
display_contacts_button.pack(pady=10)

def main():
    display_contacts()

main()

root.mainloop()