correct_username = "abhi"
correct_password = "5678"
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == correct_username and password == correct_password:
    print("Login Successful!")
elif username != correct_username and password == correct_password:
    print("Invalid Username!")
elif username == correct_username and password != correct_password:
    print("Invalid Password!")
else:
    print("Invalid Username and Password!")