username = input("Enter Username\n")
password = input("Enter password\n")

if (username == "rohit" and password == "pass123"):
    print("LOGIN SUCCESSFULL")
elif (username != "rohit"):
    print("Invalid username..!")
else:
    print("Wrong password..!")