# Write some code and hack the planet!
# Author: nucular moo

import re

# 1. We create a string of the alphabet

def alphabet():

    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

    #print(alphabet)

    a = alphabet.split()

    #print(len(a))

    return a

# 2. We create a list of numbers from 1-26

def numbers():

    a = alphabet()

    #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    #           15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    beginning = 1

    end = len(a) + 1

    #print end
    #
    # Why is end 27 and not 26?

    numbers = list(range(beginning, end))

    #print(numbers)

    return numbers

# 3. We combine the alphabet with the numbers to form a dictionary

def caesar_key():

    values = alphabet()
    keys = numbers()

    caesar = dict(zip(keys, values))

    #keys: numbers
    #values: letters

    #print(caesar)

    return caesar

# 4a. We return the letter corresponding to a number

def number_to_letter(number):

    caesar = caesar_key()

    letter = caesar[number]

    #print(letter)

    return letter

# 4b. We return the number corresponding to a letter

def letter_to_number(letter):

    caesar = caesar_key()

    inv_caesar = {value: key for key, value in caesar.items()}

    #print(inv_caesar)

    number = inv_caesar[letter]

    #print(number)

    return number

# 5. Encryption

def encode(plaintext):

    print("")

    encoding = ""
    for letter in plaintext:
        if letter == ' ':
            continue
        else:
            encoding = encoding + str(letter_to_number(letter.upper())) + " "

    #print(encoding)

    return encoding

# 6. Decryption

def decode(encrypted_text):

    plaintext = ""
    for number in encrypted_text:
        if number == ' ':
            plaintext = plaintext + ' '
        else:
            plaintext = plaintext + number_to_letter(int(number))


    return plaintext

# 7. Validate input string

def validate(string, switch):

    answer = 1

    if switch is 'e':
        print("Validating input before encoding...")
        answer = validate_spaces(string)
        answer = validate_string(string)
    elif switch is 'd':
        print("Validating input before decoding...")
        answer = validate_number(string)

    if answer is 1:
        print("Done.")

    return answer

# 7.1

def validate_spaces(string):
    m = re.search(r'\s{2,}', string)
    if m:
        print("ERROR: Invalid amount of spaces, terminating...")
        return 0
    else:
        return 1

# 7.2

def validate_string(string):

    a = alphabet()

    for c in string:
        if c is ' ':
            continue
        if c not in a:

            print("ERROR: Invalid characters, terminating..")
            return 0

    return 1

# 7.3

def validate_number(string):

    for number in string:
        try:
            int(number)
        except ValueError:

            print("ERROR: Invalid number, terminating...")
            return 0

    return 1

# 8. Welcome screen

def welcome():

    print("")
    print("")
    print("<><><><>Welcome to the amazing Caesar encryption/decryption tool!<><><><>")
    print("")
    print("")

# 9. Interface

def menu():

    encoding = ('E', 'e')
    decoding = ('D', 'd')
    quit = ('Q, q')

    while(1):

        welcome()

        command = raw_input('(E)ncode/(D)ecode/(Q)uit?: ')
        print("")
        print("")

        #print(command)

        if command in quit:

            exit()

        if command in encoding:
            print("For encryption, sentences can be formed using the alphabet and spaces")
            print("")
            print("")

            plaintext = raw_input('Please input message: ')
            plaintext = plaintext.upper()
            answer = validate(plaintext, 'e')
            if not answer:
                continue
            elif answer:
                encrypted_text = encode(plaintext)
                print("Your encrypted message:")
                print("")
                print(encrypted_text)

        elif command in decoding:
            print("For decryption, please use the following format: 13 1 14 1 20 8 5 3 15 18 7 9")
            print("")
            print("")
            plaintext = raw_input('Please input message: ')
            plaintext = plaintext.split()

            answer = validate(plaintext, 'd')
            if not answer:
                continue
            else:
                decrypted_text = decode(plaintext)
                print("")
                print("Your decrypted message: ")
                print("")
                print(decrypted_text)


def main():
    #alphabet()
    #numbers()
    #caesar_key()
    #number_to_letter(5)
    #letter_to_number('R')

    menu()

if __name__ == "__main__":
    main()
