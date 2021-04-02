import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100:=>"))
while guess != number:
    if guess < number:
        print("Please Guess a number higher")
        guess = int(input("Guess a number between 1 and 100:=>"))
    else:
        print("Please guess a number lower")
        guess = int(input("Guess a number between 1 and 100:=>"))
print("Congratulation You Won!!")