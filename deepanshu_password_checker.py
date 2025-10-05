

# Defining a function to check upper case letter

def check_uppercase(pwd):
    has_upper = False
    for i in pwd:
        if i.isupper():
            has_upper = True
    
    if has_upper:
        return True
    else:
        return False

# Defining a function to check lower case letter

def check_lowercase(pwd):
    has_lower = False
    for i in pwd:
        if i.islower():
            has_lower = True

    if has_lower:
        return True
    else:
        return False

# Defining a function to check numbers

def check_numbers(pwd):
    has_numbers = False
    for i in pwd:
        if i.isdigit():
            has_numbers = True
    
    if has_numbers:
        return True
    else:
        return False

# Defining a function to check special charachter

def check_special_char(pwd):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    has_specialchar = False
    for i in pwd:
        if i in special_characters:
            has_specialchar = True

    if has_specialchar:
        return True
    else:
        return False

# Defining a function to check lenght of password

def check_length(pwd):
    if len(pwd) >= 8:
        return True
    else:
        return False
   

# Taking password from user
password = input("Enter your password: ")

# Check the strength
if check_uppercase(password) and check_lowercase(password) and check_numbers(password) and check_special_char(password) and check_length(password):
    print("Strong Password: Your password meets all the requirements")

elif check_uppercase(password) == False:
    print("Weak Password. Please include: Upper Case Letters")

elif check_lowercase(password) == False:
    print("Weak Password. Please include: Lower Case Letters")

elif check_numbers(password) == False:
    print("Weak Password. Please include: Numbers")

elif check_special_char(password) == False:
    print("Weak Password. Please include: Special Charachters")

elif check_length(password) == False:
    print("Weak Password. Password doesn't meet length criteria")

else:
    print("Please check the criteria, your password doesn't meet one or more criteria")
