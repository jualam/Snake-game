'''
1 for snake
-1 for water
0 for gun

'''
import random
computer=random.randint(-1,1)
youStr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youDict[youStr]
loseset={-1,2}
print(f"You choose: {reversedict[you]}\nComputer choose: {reversedict[computer]}")
if (computer==you):
    print("tie")
else:
    if ((computer-you) in loseset):
        print("Computer wins")
    else:
        print("You win")