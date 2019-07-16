# Write some code and hack the planet!
# Author: nucular moo

def hello_world():
    print("Hello world!")

def twist():
    hello = "world!"
    world = "Hello "

    print(world + hello)

def turn():
    helloworld_as_a_list = ["H", "e", "l", "l", "o", " ", "w","o", "r", "l", "d", "!"]

    helloworld = ""

    for x in helloworld_as_a_list:
        helloworld += x

    print(helloworld)

def shake():

    a = "abcdefghijklmnopqrstuvwxyz.?! "

    helloworld_alphabet_coordinates = [7, 4, 11, 11, 14, 29, 22, 14, 17, 11, 3, 28]

    hw = ""
    for index in helloworld_alphabet_coordinates:
        if not hw:
            hw += a[index].upper()
        else:
            hw += a[index]

    print(hw)

def menu():

    while(1):
        options()

def options():
    number=input("1, 2, 3 or 4? ")
    if number == (1):
        twist()
    elif number == (2):
        turn()
    elif number == (3):
        shake()
    elif number == (4):
        hello_world()
    elif number == (0):
        exit()

def main():

    menu()

if __name__ == "__main__":
    main()
