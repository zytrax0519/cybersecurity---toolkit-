password = input("Enter your password: ")

if len(password) >= 8:
    print("Password length is acceptable.")
else:
    print("Password is too short.")