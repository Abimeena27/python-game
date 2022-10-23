import random 


while 1:
    me=input("Choose:\nROCK\nPAPER\nSCISSOR\n")
    me=me.lower()
    if((me!="rock")and(me!="paper")and(me!="scissor")):
        print("Enter a valid choice")
        



    opponent=random.choice(["rock","paper","scissor"])
    if me==opponent:
        print("Tie")
        continue
    elif((me=="rock")and(opponent=="scissor")):
        print("Victory")
        break

    elif((me=="scissor")and(opponent=="paper")):
        print("Victory")
        break
    elif((me=="paper")and(opponent=="rock")):
        print("Victory")
        break
    else:
        print("DEFEATED")
        continue
    
