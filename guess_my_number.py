
import random 
number=random.randint(0,50)

def funksion():
    



    num=int(input("Guess my number:"))

    if (num<number):
        print("higher")
        funksion()
    elif (num>number):
        print("lower")
        funksion()
    else:
        print("You found it! ")
        
        ans=input("Do you want to try again: Y/N")
    while(ans=="Y"or"y"):
        funksion()

funksion()




