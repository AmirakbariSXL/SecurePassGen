#SXL
import random
import string

# Set the password length
password_length = 8

# Use all alphanumeric characters
characters = string.ascii_letters + string.digits + string.punctuation

# Initialize an empty string for the password
password = ""

# Generate the password
for index in range(password_length):
    password += random.choice(characters)

# Print the generated password
print("Password generated:", password)