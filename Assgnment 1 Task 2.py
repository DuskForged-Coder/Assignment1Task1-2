firstname = input("Enter your first name: ")
middlename = input("Enter your middle name (or press Space & then press Eenter if none): ")

if middlename == 0:
    print("No middle name entered.")
else:
    lastname = input("Enter your last name: ")

# Full greeting with all three names
print("Hello", firstname,middlename,lastname + "! Welcome to the Python program.")
