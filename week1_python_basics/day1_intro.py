print("100 Years Old Calculator. Type 'q' at any time to quit.")

while True:
    name = input("Type a name: ")
    if name.lower() == 'q':
        print("Bye!")
        break

    name = name.title()

    while True:
        year = input("Type the year of birth (YYYY): ")
        if year.lower() == 'q':
            print("Bye!")
            exit()  # Exits the whole program

        try:
            year = int(year)
            year_100 = year + 100
            print(f"{name}, you will turn 100 years old in the year {year_100}.\n")
            break  # Go back to asking for a new user
        except ValueError:
            print("Invalid year. Please enter a 4-digit number.")
