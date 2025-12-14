import contact_manager
from contact_manager import ContactManager, ContactDetails

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Add Contact Details")
        print("7. View All Contact Details")
        print("8. Update Email")
        print("9. Update Address")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ContactManager.add_contact()
        elif choice == '2':
            ContactManager.view_all_contacts()
        elif choice == '3':
            ContactManager.search_contact()
        elif choice == '4':
            ContactManager.delete_contact()
        elif choice == '5':
            ContactManager.update_contact()
        elif choice == '6':
            ContactDetails.add_details()
        elif choice == '7':
            ContactDetails.view_all_details()
        elif choice == '8':
            ContactDetails.update_email()
        elif choice == '9':
            ContactDetails.update_address()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()