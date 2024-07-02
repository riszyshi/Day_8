#User Login

def register():
    name = input("Name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if username already exists
    file = open("user_login.txt", "r")
    for line in file.readlines():
        login_info = line.split()
        if username == login_info[0]:
            print("Username already exists. Please choose a different username.\n")
            return False

    # Register new user
    file = open("user_login.txt", "a")
    file.write(username + " " + password + "\n")
    print(f"{name} successfully registered...\n")
    return True

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open("user_login.txt", "r")
    for line in file.readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("Login successful!\n")
            return True
    print("Login failed.\n")
    return False

def change_password():
    username = input("Enter your username: ")
    old_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")

    file = open("user_login.txt", "r+")
    lines = file.readlines()
    for line in lines:
        login_info = line.split()
        if username == login_info[0] and old_password == login_info[1]:
            lines = username + " " + new_password + "\n"
            file.seek(0)
            file.writelines(lines)
            print("Password changed successfully!\n")
            return True
    print("Password change failed.\n")
    return False

while True:
    print("Welcome to my User Login!")
    print("Menu:")
    print("1. Register | 2. Login | 3. Change Password")

    menu = input("Command: ")

    if menu == "1":
        register()
    elif menu == "2":
        login()
    elif menu == "3":
        change_password()
    else:
        print("Invalid output\n")