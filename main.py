import contact_manager
from contact_manager import ContactManager, ContactDetails

while True:
    print("1.Add Contact")
    print("2.View All Contacts")
    print("3.Delete Contact")
    print("4.Update Contact")
    print("5.Add Contact Details")
    print("6.View All Contact Details")
    print("7.Update Email")
    print("8.Update Address")
    print("9.Exit")

    choice=input("Enter your choice: ")
    
    if choice == '1':
        ContactManager.add_new_contact()
    elif choice == '2':
        ContactManager.view_contacts()
    elif choice == '3':
        ContactManager.delete_contact()
    elif choice =='4':
        ContactManager.update_contact()
    elif choice== '5':
        ContactDetails.add_details()
    elif choice == '6':
        ContactDetails.view_all_details()
    elif choice== '7':
        ContactDetails.update_email()
    elif choice == '8':
        ContactDetails.update_address()
    elif choice == '9':
        break
    else:
        print("Invalid choice, please try again.")
