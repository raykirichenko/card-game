import random

winning = True

while winning:
    hidden = random.randrange(1, 13)

    print("My card is: " + str(hidden))
    guess = int(input("Type 1 to draw a random card. \nIf it's higher, you win. \nIf it's lower, you lose. \nType 2 to quit. What do you choose? "))

    if guess == 1:
        mycard = random.randrange(1, 13)
        print("Your card is: " + str(mycard))
        if mycard > hidden:
            print("You win!\n")
        else:
            print("You lose!")
            winning = False
    else:
        print("Bye!")
        winning = False