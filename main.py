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

print(f"You choose: {reversedict[you]}\nComputer choose: {reversedict[computer]}")
if (computer==you):
    print("tie")
else:
    if(computer ==-1 and you==1):
        print("you win")
    elif(computer ==-1 and you==0):
        print("you lose")
    elif(computer ==1 and you==-1):
        print("you lose")
    elif(computer ==1 and you==0):
        print("you win")
    elif(computer ==0 and you==-1):
        print("you win")
    elif(computer ==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")