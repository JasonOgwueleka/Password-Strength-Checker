# Empty dictionary for login details
login_details = {}

username = input("Please enter your username: ")
password = input("Please enter your password: ")
email = input("Please enter your email: ")

# Check for spaces in any input
if " " in username or " " in password or " " in email:
    print("Invalid input. Username, password, and email cannot contain spaces.")
else:
    # Check if the password is valid
    if len(password) < 8 or not any(char.isdigit() for char in password):
        print("Invalid password. It must be at least 8 characters long and contain at least one number.")
    else:
        # Check password strength
        if (len(password) < 8 or
            not any(char.isupper() for char in password) or
            not any(char.islower() for char in password) or
            not any(char.isdigit() for char in password)):
            print("Weak password. It must include uppercase, lowercase, and a number.")
        else:
            # If everything is valid, save the info into the dictionary
            login_details["username"] = username
            login_details["password"] = password
            login_details["email"] = email

            # Add password to a list
            password_list = [password]

            #Output
            print("\nAccount created successfully!")
            print(f"Welcome to the club, {username}! " + "Your account details are:")
            print("--------------------------------------------------------")
            print(f"Username: {username}")
            print(f"Email: {email}")







