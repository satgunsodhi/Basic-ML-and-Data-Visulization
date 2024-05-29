from random import randint

value = randint(0,100)
while 1:
    i = int(input())
    if(i == value):
        print("Correct!")
        break
    if value < i:
        print("Too high")
    elif value > i:
        print("Too low") 