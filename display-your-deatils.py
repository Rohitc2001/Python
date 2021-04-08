                        # A simple program to enter and print your details.
def details(name,age,gender,add):
    print("\nName : ",name)
    print("Age : ",age,"Years")
    print("Gender : ",gender)
    print("Address : ",add)


name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
gender = input("Enter your Gender : ")
add = input("Enter your Address : ")

details(name,age,gender,add)