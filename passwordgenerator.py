import random

# Lists of characters
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']

print("Welcome to the Password Generator!")

# User input for the number of each type of character
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

# Empty string to store the password
password = ""

# Adding random letters to the password
for char in range(1, num_letters + 1):
    password += random.choice(letters_list)

# Adding random numbers to the password
for char in range(1, num_numbers + 1):
    password += random.choice(numbers_list)

# Adding random symbols to the password
for char in range(1, num_symbols + 1):
    password += random.choice(symbols_list)

# Shuffle the password to make it more random
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your generated password is: {password}")



        