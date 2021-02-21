import random
playerCash = float(input("Please enter how much money you want to play with:"))

while playerCash > 0:
    #get useer input 
    playerNum = int(input("Pick your number:"))
    #get users bet amount & check that it is valid
    playerBet = float(input("Place your bet:"))
    
    
    #validate user input
    validInput = True
    if playerBet > playerCash:
        print("You do not have enough cash to make that bet - You have R" + str(playerCash) + " remaining")
        validInput = False
        
    if playerNum > 49 or playerNum < 0:
        print("Please enter a valid number")
        validInput = False
        
    if validInput == True:
    
        #generate random number
        rouletteNum = 0
        rouletteNum = random.randint(0, 49)
    
        if playerNum == rouletteNum:
            print("You win!")
            playerCash += (playerBet * 50)
        else:
            print("Sorry you didn't win" + "\n The winning number was " + str(rouletteNum))
            playerCash -= playerBet
