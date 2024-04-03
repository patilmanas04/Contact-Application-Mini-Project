import json

contacts = []

# Retriving saved contacts from 'contacts_store.json' file
with open('contacts_store.json', 'r+') as retrived_contacts_file:
    retrived_contacts = retrived_contacts_file.read()

    if retrived_contacts:
        contacts = json.loads(retrived_contacts)
    else:
        contacts = []

# Updating 'contacts_store.json' file
def update_contacts_file():
    with open('contacts_store.json', 'w') as contact_file:
        contact_file.write(json.dumps(contacts))

# Adding new contact to contacts list
def add_contact(name, email, phone_number):
    contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number
    }

    for existing_contact in contacts:
        if existing_contact['name'].lower() == name.lower():
            print("Contact already exists.")
            return

    contacts.append(contact)

    update_contacts_file()

# Searching contact with a search term
def search_contact(name):
    searched_contacts = []
    for contact in contacts:
        if name.lower() in contact['name'].lower():
            searched_contacts.append(contact)

    return searched_contacts

# Deleting contact from contacts list
def delete_contact(contact):
    contacts.remove(contact)

    update_contacts_file()

# Updating contact details
def update_contact(contact, name, email, phone_number):
    contact['name'] = name
    contact['email'] = email
    contact['phone_number'] = phone_number

    update_contacts_file()

# Opening contact details
def open_contact(contact_name):
    contact = search_contact(contact_name)[0]
    print(f"\nContact Details -->\nName: {contact['name']}\nEmail: {contact['email']}\nPhone Number: {contact['phone_number']}")
    return contact

# Displaying contacts
def load_contacts():
    if not contacts:
        print("No Contacts Found.")
    else:
        print("Contacts -->")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']}")

# Displaying searched contacts
def display_searched_contacts(contacts):
    print("\nSearched Contacts -->")
    if not contacts:
        print("No Contacts Found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']}")

# Switching between options
def switch(option):
    if option == 1:
        name = input("Enter name:")
        email = input("Enter email: ")
        phone_number = int(input("Enter phone number: "))
        add_contact(name, email, phone_number)
        print(f"Contact Added [Added Contact: {name}]")
    elif option == 2:
        search_term = input("Enter search term: ")
        searched_contacts = search_contact(search_term)
        display_searched_contacts(searched_contacts)
    elif option == 3:
        contact_name = input("Enter contact name: ")
        opened_contact = open_contact(contact_name)

        while True:
            print("\nOptions:")
            print("1. Edit Contact ✏️")
            print("2. Delete Contact 🗑️")
            print("3. Go Back 🔙")

            option = int(input("Enter option number: "))
            print()

            if option == 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone_number = int(input("Enter phone number: "))
                update_contact(opened_contact, name, email, phone_number)
                print("Contact Updated.")
                print("Updated Contact Details ==>")
                print(f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}")
            elif option == 2:
                delete_contact(opened_contact)
                print(f"Contact Deleted [Deleted Contact: {opened_contact['name']}]")
            elif option == 3:
                break
            else:
                print("Invalid Option.")
    elif option == 4:
        load_contacts()
    elif option == 5:
        print("-------------------------------- Exiting Application 🔚  --------------------------------")
        exit()
    else:
        print("Invalid Option!!")

def main():
    print("--------------------------- Welcome to Contact Application ☎️  ---------------------------\n")

    # Loading saved contacts
    load_contacts()

    # Displaying options
    while True:
        print("\nOptons:")
        print("1. Add Contact ➕")
        print("2. Search Contact 🔎")
        print("3. Open Contact 📂")
        print("4. Display Contacts 📋")
        print("5. Exit 🔚")
    
        option = int(input("Enter option number: "))
        print()

        switch(option)

main()