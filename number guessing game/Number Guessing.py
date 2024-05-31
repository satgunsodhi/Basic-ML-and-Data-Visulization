from random import randint

# taking a random number from 1 to 100 from the random library
value = randint(0,100)

# game code
while 1:
    i = int(input())
    if(i == value):
        print("Correct!")
        break
    if value < i:
        print("Too high")
    elif value > i:
        print("Too low")