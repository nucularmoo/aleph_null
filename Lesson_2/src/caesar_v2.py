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

# 2.1 We rotate the numbers accordingly

def numbers_rotated(rotation):
    #rotation = 5
    n = numbers()
    first_half = n[int(rotation):len(n)]
    second_half = n[0:int(rotation)]
    rotation = first_half + second_half
    #print(rotation)
    return rotation

# 2.2 Rotation

def rotation():
    r = 0
    while not r:
        rotation = raw_input('Please input Caesar rotation (1-25): ')
        print("Validating rotation before proceeding...")
        r = validate_rotation(rotation)

    print_done()

    return rotation

# 3. We combine the alphabet with the numbers to form a dictionary

def caesar_key(r):

    values = alphabet()
    keys = numbers_rotated(r)

    caesar = dict(zip(keys, values))

    #keys: numbers
    #values: letters

    #print(caesar)

    return caesar

# 4a. We return the letter corresponding to a number

def number_to_letter(number, r):

    caesar = caesar_key(r)

    letter = caesar[number]

    #print(letter)

    return letter

# 4b. We return the number corresponding to a letter

def letter_to_number(letter, r):

    caesar = caesar_key(r)

    inv_caesar = {value: key for key, value in caesar.items()}

    #print(inv_caesar)

    number = inv_caesar[letter]

    #print(number)

    return number

# 5. Encryption

def encode(plaintext, r):

    empty_line()

    encoding = ""
    for letter in plaintext:
        if letter == ' ':
            continue
        else:
            encoding = encoding + str(letter_to_number(letter.upper(), r)) + " "

    #print(encoding)

    return encoding

# 6. Decryption

def decode(encrypted_text, r):

    empty_line()

    plaintext = ""
    for number in encrypted_text:
        if number == ' ':
            plaintext = plaintext + ' '
        else:
            plaintext = plaintext + number_to_letter(int(number), r)


    return plaintext

# 7. Validate input string

def validate(string, switch):

    answer = 1

    if switch is 'e':

        print(validate_print_input("en"))
        answer = validate_spaces(string)

        if answer is 0:
            return answer

    elif switch is 'd':

        print(validate_print_input("de"))
        answer = validate_number(string)

    if answer is 1:
        print_done()

    return answer

# 7.1

def validate_spaces(string):
    m = re.search(r'\s{2,}', string)
    if m:
        print(validate_print_error("number of spaces"))

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

            validate_print_error("characters")

            return 0

    return 1

# 7.3

def validate_number(string):

    for number in string:
        try:
            int(number)
        except ValueError:

            validate_print_error("number")

            return 0

    n = numbers()

    for number in string:
        if int(number) not in n:

            validate_print_error("number")

            return 0

    return 1

# 7.4

def validate_rotation(rotation):

    n = numbers()
    for number in rotation:
        try:
            int(number)
        except ValueError:
            print("ERROR: Invalid number")
            return 0
    if int(rotation) not in n[0:len(n)-2]:

        print("ERROR: Invalid rotation integer")
        return 0

    return 1

# 7.5.1

def validate_print_error(id):

    print("ERROR: Invalid " + id + ", terminating...")

# 7.5.2

def validate_print_input(t):

    print("Validating input before " + t + "coding...")

# 8. Welcome screen

def welcome():

    empty_line()
    empty_line()
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>_<><><><>")
    print("<><><><> Welcome to the amazing Caesar encryption/decryption tool! <><><><>")
    print("<><><><><><><><>_<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    empty_line()
    empty_line()

def welcome_line_generator():

    diamond = "<>"
    line = "_"

    #start, end = # 4 times diamond

    # 29 times diamond one time _

# 8.1. Help

def halp():
    print("help is coming")

# 8.2 Encrypting

def encrypt():

    r = rotation()
    plaintext = encrypt_body()
    answer = validate(plaintext, 'e')

    if not answer:
        return

    elif answer:
        encrypted_text = encode(plaintext, r)
        empty_line()
        print("Your encrypted message:")
        empty_line()
        print(encrypted_text)

# 8.2.1

def encrypt_body():
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>_<><><><><>")
    print("<> For encryption, sentences can be formed using the alphabet and spaces <>")
    print("<><><><><><><><_><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    empty_line()
    empty_line()

    plaintext = raw_input('Please input message: ')
    plaintext = plaintext.upper()

    return plaintext

# 8.3 Decrypting

def decrypt():

    r = rotation()
    plaintext = decrypt_body()
    answer = validate(plaintext, 'd')

    if not answer:
        return
    else:
        decrypted_text = decode(plaintext, r)
        empty_line()
        print("Your decrypted message: ")
        empty_line()
        print(decrypted_text)

# 8.3.1

def decrypt_body():

    empty_line()
    print("<><><><><><><><><><><><><><><><><><><><><><><><><_><><><><><><><><><><><><><><><><>")
    print("<> For decryption, please use the following format: 13 1 14 1 20 8 5 3 15 18 7 9 <>")
    print("<><><><><><><><><><><><><><>_<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    empty_line()
    empty_line()
    plaintext = raw_input('Please input message: ')
    empty_line()
    plaintext = plaintext.split()

    return plaintext

# 9. Interface

def menu():

    encoding = ('E', 'e')
    decoding = ('D', 'd')
    quit = ('Q, q')
    help = ('H', 'h')

    while(1):

        welcome()

        command = raw_input('(E)ncode/(D)ecode/(H)elp/(Q)uit?: ')
        empty_line()
        empty_line()

        #print(command)

        if command in quit:

            exit()

        elif command in help:

            halp()

        elif command in encoding:

            encrypt()

        elif command in decoding:

            decrypt()

# 9.1 Print empty line

def empty_line():
    print("")

# 9.2 Print done

def print_done():
    print("Done.")
    empty_line()

# M:A:I:N #

def main():

    menu()

if __name__ == "__main__":
    main()
