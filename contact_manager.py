
import  mysql.connector as m
con=m.connect(host="localhost",user="root",password="root",database="contacts_database")
cursor=con.cursor()
d={'india':'+91','usa':'+1','uk':'+44','australia':'+61','canada':'+1','dubai':'+971','china':'+86','japan':'+81','germany':'+49','france':'+33'}

class ContactManager:
    def __init__(self,name,phone,country):
        self.name=name
        self.phone=phone
        self.country=country

    def add_new_contact(self):
        name = input("enter name:")
        phone = input("enter phone number:")
        country = input("enter country:").lower()
        if country in d:
            country_code = d[country]
            if country == 'india' and len(phone) != 10:
                print("invalid phone number for india")
            elif country == 'usa' and len(phone) != 10:
                print("invalid phone number for usa")
            elif country == 'uk' and len(phone) != 10:
                print("invalid phone number for uk")
            elif country == 'australia' and len(phone) != 9:
                print("invalid phone number for australia")
            elif country == 'canada' and len(phone)!= 10:
                print("invalid phone number for canada")
            elif country == 'dubai' and len(phone)!= 9:
                print("invalid phone number for dubai")
            elif country == 'china' and len(phone) != 11:
                print("invalid phone number for china")
            elif country == 'japan' and len(phone) != 10:   
                print("invalid phone number for japan")
            elif country == 'germany' and len(phone)!= 11:
                print("invalid phone number for germany")
            elif country == 'france' and len(phone) != 9:
                print("invalid phone number for france")
            else:
                    q1='insert into  contact values(%s,%s,%s)'
                    v1=(name,country_code,phone)
                    cursor.execute(q1,v1)
                    con.commit()
                    print("contact added successfully") 

    def view_contacts(self):
        q2='select * from contact'
        cursor.execute(q2)
        result=cursor.fetchall()
        for row in result:
            print("Name:",row[0])
            print("Country Code:",row[1])
            print("Phone Number:",row[2])     

    def delete_contact(self):
        name = input("enter the name of the contact to delete: ")
        q3='delete from contact where name=%s'
        v3=(name,)
        cursor.execute(q3,v3)
        con.commit()
        print("contact deleted successfully")

    def update_contact(self):
        name = input("enter the name of the contact to update: ")
        new_phone = input("enter the new phone number: ")
        country = input("enter country: ").lower()
        if country in d:
            country_code = d[country]
            q4='update contact set country_code=%s, phone_number=%s where name=%s'
            v4=(country_code,new_phone,name)
            cursor.execute(q4,v4)
            con.commit()
            print("contact updated successfully")

class ContactDetails(ContactManager):
    def __init__(self, name, email, address):
        super().__init__(name, None, None)
        self.email = email
        self.address = address

    def add_details():
        name = input("enter name: ")
        email = input("enter email: ")
        address = input("enter address: ")
        q5='insert into contact_details values(%s,%s,%s)'
        v5=(name,email,address)
        cursor.execute(q5,v5)
        con.commit()
        print("details added successfully")

    def view_all_details():
        q6='select * from contact natural join details'
        cursor.execute(q6)
        result=cursor.fetchall()    

    def update_email():
        name = input("enter the name of the contact to update email: ")
        new_email = input("enter the new email: ")
        q7='update contact_details set email=%s where name=%s'
        v7=(new_email,name)
        cursor.execute(q7,v7)
        con.commit()
        print("email updated successfully")

    def update_address():
        name = input("enter the name of the contact to update address: ")
        new_address = input("enter the new address: ")
        q8='update contact_details set address=%s where name=%s'
        v8=(new_address,name)
        cursor.execute(q8,v8)
        con.commit()
        print("address updated successfully")   

