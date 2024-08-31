import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"Contact(Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address})"

class ContactManager:
    def __init__(self, data_file='contacts.json'):
        self.data_file = data_file
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact.__dict__)
        self.save_contacts()
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, query):
        results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print(f"Current details: {contact}")
                contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
                self.save_contacts()
                print(f"Contact {contact['name']} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact {contact['name']} deleted successfully!")
                return
        print("Contact not found.")

def user_interface():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            query = input("Enter name or phone number to update: ")
            manager.update_contact(query)

        elif choice == '5':
            query = input("Enter name or phone number to delete: ")
            manager.delete_contact(query)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()
