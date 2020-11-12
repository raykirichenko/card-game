import random

winning = True
score = 0

while winning:
    hidden = random.randrange(1, 13)

    print("My card is: " + str(hidden))
    guess = int(input("Type 1 to draw or 2 to quit: "))

    if guess == 1:
        mycard = random.randrange(1, 13)
        print("Your card is: " + str(mycard))
        if mycard > hidden:
            print("You win!")
            score = score + 100
            print("Your score: " + str(score) + "\n")
        else:
            print("You lose!")
            print("Final score: " + str(score) + "\n")
            winning = False
    else:
        print("Good game!")
        winning = False