import random
playing = True
number = str(random.randint(10,20))
print("I will genarate a number between 10 to 20.")

while playing:
    guess = input("Give me your best guess : \n")
    if number == guess:
        print("You win the game!!!")
        print("The number was", number)
        break
    else:
        print("Try Again")
