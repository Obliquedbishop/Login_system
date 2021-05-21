def login(email, password):
    success = False
    file = open("user_details.txt", "r")
    for credentials in file:
        registered_email, registered_password = credentials.split(";")
        registered_email = registered_email.strip()
        if email == registered_email:
            success = True
            break
        file.close()
        if success:
            print("Login Successful!!!")


def register(username, email, password):
    file = open("user_details.txt" , 'a')
    file.write("\n"+username+","+email+";"+password)
    file.close()
    print(username + " you got yourself registered successfully")


def email_check(email):

    count_1 = 0
    for char in email:
        if char == "@":
            count_1 += 1
    if count_1 == 1:
        name, domain = email.split("@")
        import string
        uppercase_string = string.ascii_uppercase
        lowercase_string = string.ascii_lowercase
        numbers_string = string.digits
        allowed_string = uppercase_string + lowercase_string + numbers_string + '.'
        for char in name:
            if char in allowed_string:
                pass
            else:
                return "wrong"
        for char in domain:
            if char in allowed_string:
                pass
            else:
                return "wrong"
    else:
        return "wrong"

    success = False
    file = open("user_details.txt" , "r")
    for credentials in file:
        registered_email, registered_password = credentials.split(";")
        registered_email = registered_email.strip()
        if email == registered_email:
            success = True
            break
        file.close()
        if success:
            return "exists"
        else:
            return "verified new user"


def password_check(password):
    if len(password) < 15:
        return "short"
    else:
        from suggest_password import check
        if check(password) == "weak":
            return "weak"


def register_access():
    print("Register yourself")
    username = input("Enter your username\n")

    #  inputting email address
    flag = 0
    while flag == 0:
        email = input("Enter your email address\n")
        if email_check(email) == "wrong":
            print("Please enter a valid email address")
        elif email_check == "exists":
            print("The email already exists, Please enter a new one")
        else:
            flag = 1

    # inputting password
    flag = 0
    while flag == 0:
        password = input("Enter your password\n")
        if password_check(password) == "short":
            print("Please enter the password at least 15 characters long")
        elif password_check(password) == "weak":
            print("Please enter a stronger password")
            from suggest_password import suggestion
            suggestion(15)
        else:
            flag = 1
    register(username, email, password)


def login_access():
    print("Login Yourself")
    email = input("Enter your email address\n")
    password = input("Enter your password\n")
    login(email, password)


def begin():
    print("Welcome to my program")
    option = input("Are, you a new user [Y/N]\n")
    if option != 'Y' and option != 'N':
        print("Please, enter the correct option")
        begin()
    elif option == 'Y':
        register_access()
    else:
        login_access()


begin()