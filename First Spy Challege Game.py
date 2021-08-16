print('''   ,a8888a,       ,a8888a,  888888888888
 ,8P"'  `"Y8,   ,8P"'  `"Y8,        ,8P'
,8P        Y8, ,8P        Y8,      d8"
88          88 88          88    ,8P'
88          88 88          88   d8"
`8b        d8' `8b        d8' ,8P'
 `8ba,  ,ad8'   `8ba,  ,ad8' d8"
   "Y8888P"       "Y8888P"  8P'
''')
print("Welcome to the dungeon of Tarzakin")
print("In this game, you will have up too 4 options at most choose op1, op2, op3, or op4")
print("Embark upon a journey to discover the fallen detective, the item they possess is a wonder beyond this world! Depart!")

option1 = (input("You arrive, at an abandoned temple with a half open door before you. Do you go open it(op1) or find another way in?(op2)?\n")).lower()


if option1 == "op1":
    print("You enter and find the plaace is torn and shredded.")
    option2 = input("You progress into the temple and find a lever at the side of the wall(op1) and see a book on the ground with symbols on its back(op2) and notice something in the shadows(op3) which do you investigate?\n").lower()
    if option2 == "op1":
        print("The lever releases spikes and pierce you")
        print("YOU ARE DEAD")
    elif option2 == "op2":
        print("You pick up the book and hear something unlock behind you, a hidden passage! You walk towards it.")
        option3 = input("You go down into an underground tunnel, you see two path ways left(op1) and right(op2), which way do you go?\n").lower()
        if option3 == "op1":
            print("You go left and find a skeleton, it appears to be of someone long dead.")
            option4 = input("You kneel over the body, see the relic do you take it slowly(op1) or quickly(op2)?\n").lower()
            if option4 == "op2":
                print("You take the relic and escape unscaved!")
                print("YOU WIN!")
            else:
                print("The skeleton awakens and sees you, it pierces your heart with the relic!")
                print("YOU ARE DEAD")
        else:
            print("A knight falls from above and smites your head!")
            print("YOU ARE DEAD!")
    else:
        print("You die by the spirits of the fallen shadows")
        print("YOU ARE DEAD")
else:
    print("You are assaulted by a beefy man and beated")
    print("YOU ARE DEAD")
