import string
import random
import array

def generate_password(length, character_sets):
    digits = '0123456789'
    lcase_chars = string.ascii_lowercase
    ucase_chars = string.ascii_uppercase
    symbols = '@#$!^&:?.|~*'

    # Combine all character sets into one array
    combined_list = list(digits + lcase_chars + ucase_chars + symbols)

    # Ensure at least one character from each set
    rand_digit = random.choice(digits)
    rand_lower = random.choice(lcase_chars)
    rand_upper = random.choice(ucase_chars)
    rand_symbol = random.choice(symbols)

    # Combine the selected characters
    temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

    # Fill the rest of the password length by selecting randomly from the combined list
    for _ in range(length - 4):
        temp_pass += random.choice(combined_list)

    # Convert temporary password into array and shuffle
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    # Traverse the temporary password array and append the characters to form the password
    password = ''.join(temp_pass_list)
    return password

def main():
    print("Password Generator")
    print("-------------------")

    while True:
        user_selection = input("Do you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")
        
        if user_selection.lower() == 'n':
            print("Thank You! See you next time.")
            break
        elif user_selection.lower() == 'y':
            length = int(input("Enter the length of the Password: "))
            characterList = ""

            while True:
                print('''Choose character set for password from these: 
                    1. Digits
                    2. Letters
                    3. Special characters
                    4. All above
                    5. Exit''')
                
                choice = int(input("Pick a number "))
                
                if choice == 5:
                    break
                if choice == 4:
                    characterList = string.ascii_letters + string.digits + string.punctuation
                    break
                
                if choice in range(1, 4):
                    characterList += character_sets[choice]
                else:
                    print("Please pick a valid option!")

            password = generate_password(length, characterList)
            print("A randomly generated Password is:", password)
            print("")
        else:
            print("Invalid Input! Try Again.")
            print("")

if __name__ == "__main__":
    character_sets = {
        1: string.digits,
        2: string.ascii_letters,
        3: string.punctuation,
    }
    main()
