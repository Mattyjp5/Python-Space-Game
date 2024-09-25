######################################################################

import pickle, shelve #The pickle model is imported as it is required to store the player's data
import random #The random model is imported so that random rewards can be given

######################################################################

class Player(object): #The player object handles all the player's statistics and changes [Dawson, 2011]

    def gameOptions(self): #The main in-game menu which allows the player to decide where to go/what to do
        gameOptionsMenu = True
        while gameOptionsMenu:
            gameOptions = input("\nWhat would you like to do?\n [1] - Travel\n [2] - Save\n [3] - View Ship\n [4] - Help\n")

            if gameOptions == "1":
                travelOptions = input("\nWhere would you like to go?\n [1] - Go to the Station\n [2] - Go the the Asteroid\n [3] - Go to the Planet\n [4] - Go to the Arena\n")

                if travelOptions == "1":

                    if position == "Station":
                        print("You are already there!")

                    else:
                        gameOptionsMenu = False
                        station.land()

                elif travelOptions == "2":

                    if position == "Asteroid":
                        print("You are already there!")

                    elif fuel < 10:
                        print("You do not have enough fuel")
                    
                    else:
                        gameOptionsMenu = False
                        player.fuelChange(-10)
                        asteroid.approach()

                elif travelOptions == "3":

                    if position == "Planet":
                        print("You are already there!")

                    elif fuel < 15:
                        print("You do not have enough fuel")
                    
                    else:
                        gameOptionsMenu = False
                        player.fuelChange(-20)
                        planet.approach()

                elif travelOptions == "4":

                    if position == "Arena":
                        print("You are already there!")

                    elif fuel < 5 and hull < 25:
                        print("You do not have enough fuel or hull")
                    
                    else:
                        gameOptionsMenu = False
                        player.fuelChange(-5)
                        arena.approach()

            elif gameOptions == "2":
                saveSystem()
                
            elif gameOptions == "3":
                player.viewShip()

            elif gameOptions == "4":
                print("The aim of the game is to get 10,000 credits to pay of a debt\n You can get credits from mining the Asteroid, exploring the Planet or battling in the Arena\n However, these activities use up your fuel/hull which has to be replenished for credits at the Station\n You can also buy upgrades to help with combat or sell mined/gathered materials for credits\n Once you have 10,000 credits you can go to the Station and pay off your debt")

            else:
                print("That is not a valid input!")
    
    def creditChange(self, change): #A function that can add or subtract a certain amount of credits to/from the player
        global credits
        credits += change
        print("Your account balance has changed by",change,"\n")
        print("Your account balance is now",credits,"\n")

    def fuelChange(self, change): #A function that can add or subtract a certain amount of fuel to/from the player
        global fuel
        fuel += change
        print("Your fuel has changed by",change,"\n")
        print("Your fuel is now",fuel,"\n")
            
    def hullChange(self, change): #A function that can add or subtract a certain amount of hull health to/from the player
        global hull
        hull += change
        print("Your hull has changed by",change,"\n")
        print("Your hull is now",fuel,"\n")

    def positionChange(self, change): #A function that change the player's position
        global position
        position.pop()
        position.append(change)
        print("Your position is now",position,"\n")

    def cargoAdd(self, material): #A function that adds a material to the player's cargo
        cargo.append(material)
        print(material,"has been added to your cargo\n")

    def cargoRemove(self, material): #A function that removes a material to the player's cargo
        cargo.remove(material)
        print(material,"has been removed to your cargo\n")

    def luck(self, min, max): #A function that generates random numbers
        randomValue = random.randint(min, max)
        return randomValue
    
    def combatPower(self): #A function that calculate the player's combat power (a statistic which dictates what kind of enemies they can take on) depending on the upgrades they've purchased
        combatPower = 100
        if "Laser Cannon" in upgrades:
            combatPower + 50

        elif "Rocket Launcher" in upgrades:
            combatPower + 100

        elif "Rail Gun" in upgrades:
            combatPower + 200

        else:
            combatPower = 100

        return combatPower

    def viewShip(self): #Prints the player's statistics
        print("Your ship has the following statistics:\n")
        print("Credits:",credits)
        print("Position:",position)
        print("Hull %:",hull)
        print("Fuel %:",fuel)
        print("Upgrades",upgrades)
        print("Cargo",cargo)

class Station(object): #The station is a place where the player can refuel, repair, buy and sell
    def land(self):
        player.positionChange("Station")
        station.options()

    def options(self): #The Station's options - allows the player to interact with the station and its components
        optionsMenu = True
        while optionsMenu:
            print("\nWelcome to the Station\n")
            stationOptions = input("What would you like to do?\n [1] - Repair/Refuel\n [2] - Buy/Sell\n [3] - Take Off\n [4] - Pay the debt\n")

            if stationOptions == "1":
                optionsMenu = False
                station.services()

            elif stationOptions == "2":
                optionsMenu = False
                station.market()
            
            elif stationOptions == "3":
                optionsMenu = False
                player.gameOptions()

            elif stationOptions == "4":
                global credits
                if credits >= 10000:
                    print("Congratulations, you have completed the game!\n")
                    player.creditChange(-10000)

                else:
                    print("You do not have enough credits for that!\n")

            else:
                print("That is not a valid input\n")

    def services(self):
        servicesOptionsMenu = True
        while servicesOptionsMenu:
            servicesOptions = input("Where would you like to go?\n [1] - Refuel\n [2] - Repair\n [3] - Exit\n")

            if servicesOptions == "1":
                refuelPrice = 100 - fuel
                print("It will cost you",refuelPrice,"to refuel")
                refuelConfirmation = input("Are you sure?\n [Y] - Yes\n [N] - No\n")
                if refuelConfirmation == "Y":
                    player.fuelChange(refuelPrice)
                    player.creditChange(-refuelPrice)
                else:
                     pass

            elif servicesOptions == "2":
                repairPrice = 100 - hull
                print("It will cost you",repairPrice,"to refuel")
                refuelConfirmation = input("Are you sure?\n [Y] - Yes\n [N] - No\n")

                if refuelConfirmation == "Y":
                    player.hullChange(repairPrice)
                    player.creditChange(-repairPrice)
            
            elif servicesOptions == "3":
                servicesOptionsMenu = False
                print("Qutting")
                station.options()

            else:
                print("That is not a valid input")

    def market(self):
        optionsMenu = True
        while optionsMenu:
            print("\nWelcome to the shop you have",credits,"credits\n")
            marketOptions = input("What would you like to do?\n [1] - Buy\n [2] - Sell\n [3] - Exit\n")

            if marketOptions == "1": #If the player choses the Buy option, the player will be able to buy upgrades with their money
                avaliableUpgrades = {"Laser Cannon" : 500, "Rocket Launcher" : 100, "Rail Gun" : 2000}
                print("Avalible upgrades are", avaliableUpgrades,"\n")
                upgradePurchase = input("Please input the name of the upgrade you'd like to purchase or input [X] to quit\n")

                try: #The program will try to match the string the player entered with an existing upgrade
                    upgradeCost = avaliableUpgrades[upgradePurchase]

                    if upgradePurchase in upgrades:
                        print("You already have that!")
                    
                    elif upgradePurchase in avaliableUpgrades and credits >= upgradeCost:
                        print("Purchased")
                        player.creditChange(-upgradeCost)
                        upgrades.append(upgradePurchase)
                        print(upgrades)
                    
                    elif upgradeCost > credits:
                        print("Sorry, you can't afford that")

                except KeyError: #This exception will trigger if the player inputs a value that isn't an upgrade listed above
                    print("That is not a valid input")
                
                finally: #Finally the loop will reset
                    pass

            elif marketOptions == "2": #If the player choses the sell option, the player can choose to sell a certain material they have gathered
                materials = {"Coal" : 50, "Iron" : 100, "Gold" : 250, "Diamond" : 500}
                print("Material prices are", materials,"\n")
                print("The materials that you can sell are",cargo,"\n")
                materialSell = input("Please input the name of the material you'd like to sell or input [X] to quit\n")

                materialValue = materials[materialSell] #The value of the material that the player wishes to sell is calculated
                materialCount = cargo.count(materialSell) #The amount of times that material appears in the cargo list is counted

                if materialSell in materials:
                        print("You sold",materialSell,"\n")
                        for i in range (materialCount): #This loop will remove all of a certain type of material from the player's cargo
                            player.creditChange(+materialValue)
                            player.cargoRemove(materialSell)
            
            elif marketOptions == "3": #If the player choses the exit option they shall return to the station menu
                optionsMenu = False
                station.options()

class Asteroid(object): #The asteroid is a place that can be mined by the player for resources
    def approach(self):
        player.positionChange("Asteroid")
        asteroid.options()

    def options(self):
        optionsMenu = True
        while optionsMenu:
            asteroidOptions = input("You see an asteroid before you, what would you like to do?\n [1] - Mine\n [2] - Go elsewhere\n")

            if asteroidOptions == "1" and fuel > 0:
                player.fuelChange(-5)
                asteroid.materialContents()

            elif asteroidOptions == "2":
                optionsMenu = False
                player.gameOptions()

            else:
                print("That is not a valid input!\n")
    
    def materialContents(self): #Randomly determines what material the asteroid will give when mined
        randomValue = player.luck(1, 113)

        if randomValue <= 50:
            player.cargoAdd("Coal")

        elif randomValue >= 51 and randomValue <= 81:
            player.cargoAdd("Iron")

        elif randomValue >= 82 and randomValue <= 102:
            player.cargoAdd("Gold")

        elif randomValue >= 103:
            player.cargoAdd("Diamond")

class Planet(object): #The planet is a place where the player has a chance to find treasure and materials
    def approach(self):
        player.positionChange("Planet")
        planet.options()

    def options(self):
        optionsMenu = True
        while optionsMenu:
            options = input("You see a planet before you, what would you like to do?\n [1] - Explore\n [2] - Go elsewhere\n")

            if options == "1" and fuel > 0:
                player.fuelChange(-20)
                planet.contents()

            elif options == "2":
                optionsMenu = False
                player.gameOptions()

            else:
                print("That is not a valid input!\n")

    def contents(self): #Randomly determines what structure the player will find and what reward the player will recieve
        randomValue = player.luck(1, 203) #This value will be used to decide which structure the player finds

        if randomValue <= 100:
            print("You scoured the planet but found nothing")

        elif randomValue >= 101 and randomValue <= 151:
            print("You scoured the planet and found a crate full of fuel")
            refuelAmount = 100 - fuel
            player.fuelChange(refuelAmount)

        elif randomValue >= 152 and randomValue <= 192:
            print("You scoured the planet and found a crate full of treasure")
            rewardValue = player.luck(100, 1000)
            player.creditChange(rewardValue)

        elif randomValue >= 193:
            print("You scoured the planet and found a crate full of diamonds")
            rewardValue = player.luck(1, 10)
            player.cargoAdd("Diamond")
            for i in range (rewardValue):
                player.cargoAdd("Diamond")

class Arena(object): #The arena is an area that allows the user to battle enemies
    def approach(self):
        player.positionChange("Arena")
        arena.options()

    def options(self):
        optionsMenu = True
        while optionsMenu:
            options = input("Welcome to the arena, what would you like to do?\n [1] - Battle\n [2] - Go elsewhere\n")

            if options == "1" and hull > 1 and fuel > 5:
                arena.battle()

            elif options == "2":
                optionsMenu = False
                player.gameOptions()

            else:
                print("That is not a valid input!\n")

    def battle(self):
        combatPower = player.combatPower() #The player's combat power is calculated
        enemyCombatMultiplier = (player.luck(50, 350))/100 #A random multiplier is generated to calculate how much stronger/weaker the enemy will be compared to the player
        enemyCombatPower = combatPower * enemyCombatMultiplier #The random multipler is then multipled by the player's combat power
        enemyCombatPower = int(enemyCombatPower) #Enemy combat power is converted to an integer so it looks nicer
        creditReward = enemyCombatPower * 2 #The player will recieve double the enemy's combat power in credits if they win the battle

        print("You see a ship infront of you, your combat power is",combatPower,"and their combat power is",enemyCombatPower)
        
        combatLoop = True
        while combatLoop:

            if combatPower <= 0: #If the players's combat power reaches 0 or lower the player loses the battle, due to how the loop works this should always be executed first
                    print("\n***You have lost the battle***\n")
                    creditReward = creditReward//4 #If the player loses they will lose half the enemy's inital combat score in credits
                    player.creditChange(-creditReward)
                    player.hullChange(-50)
                    combatLoop = False
                    arena.options()
            
            else:
                combatChoice = input("\nWhat do you do?\n [1] - Fight\n [2] - Run\n")

                if combatChoice == "1":
                    print("\n***Your turn***\n")
                    playerDamageMultiplier = (player.luck(50, 250))/100 #Calculates how more damage the player will do than normal
                    playerDamage = combatPower * playerDamageMultiplier #Calculates how much damage the player does
                    playerDamage = int(playerDamage)
                    enemyCombatPower -= playerDamage #Calculates how much combat power the enemy has left
                    print("You hit the enemy for",playerDamage,"damage")
                    print("The enemy now has",enemyCombatPower,"combat power left")
                    
                    if enemyCombatPower <= 0: #If the enemy's combat power reaches 0 or lower the player wins the battle
                        print("\n***You have won the battle!**\n")
                        player.creditChange(creditReward)
                        player.hullChange(-15)
                        combatLoop = False
                        arena.options()

                    else:
                        print("\n***Enemy's turn***\n") #Otherwise the battle will continue and the enemy will strike back
                        enemyDamageMultiplier = (player.luck(50, 125))/100 #Calculates how more damage the enemy will do than normal
                        enemyDamage = enemyCombatPower * enemyDamageMultiplier #Calculates how much damage the enemy does
                        enemyDamage = int(enemyDamage)
                        combatPower -= enemyDamage #Calculates how much combat power the enemy has left
                        print("The enemy hit you for",enemyDamage,"combat power")
                        print("You now have",combatPower,"combat power left")

                elif combatChoice == "2":
                    combatLoop = False
                    arena.options()

                else:
                    print("That is not a valid input!\n")

######################################################################

def menu():
    global playerData
    menuActive = True
    while menuActive:
        print("""

.__   __.  _______  __    __  .___________..______        ______   .__   __. 
|  \ |  | |   ____||  |  |  | |           ||   _  \      /  __  \  |  \ |  | 
|   \|  | |  |__   |  |  |  | `---|  |----`|  |_)  |    |  |  |  | |   \|  | 
|  . `  | |   __|  |  |  |  |     |  |     |      /     |  |  |  | |  . `  | 
|  |\   | |  |____ |  `--'  |     |  |     |  |\  \----.|  `--'  | |  |\   | 
|__| \__| |_______| \______/      |__|     | _| `._____| \______/  |__| \__| 
                                                                             

""") #ASCII Art which display the name of the name
                                                                                                                                                                     
        menuChoice = input("Welcome Player!\nPlease choose a save file [1-3]\n") #The player can choose which of 3 save slots to use and the program will read from a certain one
        if menuChoice == "1":
            menuActive = False #The menu loop is disabled
            try:
              saveCheck = open("Save1.dat","rb")
              saveCheck.close()
            except IOError: #If that save file does not exist, it is then created
                print("This file does not exist, creating file\n")
                playerData = shelve.open("Save1","c")
                print("File Created!\n")
                playerData.close()
                playerData = shelve.open("Save1")
                initialiseSave()
            finally:
                    playerData = shelve.open("Save1")
                    loadSystem()
        
        elif menuChoice == "2":
            menuActive = False #The menu loop is disabled
            try:
              saveCheck = open("Save2.dat","rb")
              saveCheck.close()
            except IOError: #If that save file does not exist, it is then created
                print("This file does not exist, creating file\n")
                playerData = shelve.open("Save2","c")
                print("File Created!\n")
                playerData.close()
                playerData = shelve.open("Save2")
                initialiseSave()
            finally:
                    playerData = shelve.open("Save2")
                    loadSystem()

        elif menuChoice == "3":
            menuActive = False #The menu loop is disabled
            try:
              saveCheck = open("Save3.dat","rb")
              saveCheck.close()
            except IOError: #If that save file does not exist, it is then created
                print("This file does not exist, creating file\n")
                playerData = shelve.open("Save3","c")
                print("File Created!\n")
                playerData.close()
                playerData = shelve.open("Save3")
                initialiseSave()
            finally:
                    playerData = shelve.open("Save3")
                    loadSystem()
        
        else:
            print("That is not a valid input, please try again!\n")

def loadSystem(): #[Dawson, 2011]
     global credits
     global fuel
     global hull
     global position
     global upgrades
     global cargo
    
     credits = (playerData["credits"]) #The player's credits are fetched from the shelf
     credits = str(credits) #The player's credits are converted from a list into a string
     credits = int(credits) #That string is then converted into an integer for later manipulation, I couldn't get Python to convert directly from a list into a integer

     fuel = (playerData["fuel"]) #The player's fuel is fetched from the shelf
     fuel = str(fuel)
     fuel = int(fuel) #The same above is done for fuel as it I need it to be an integer for the program to manipulate it
     
     hull = (playerData["hull"]) #The player's hull is fetched from the shelf
     hull = str(hull)
     hull = int(hull) #The same above is done for hull health as it I need it to be an integer for the program to manipulate it

     position = (playerData["position"]) #The player's position is fetched from the shelf

     upgrades = (playerData["upgrades"]) #The player's upgrades are fetched from the shelf

     cargo = (playerData["cargo"]) #The player's upgrades are fetched from the shelf

     main()

def initialiseSave(): #A default shelf is created if a new save is created
     playerData["credits"] = 1000
     playerData["fuel"] = 100
     playerData["hull"] = 100
     playerData["position"] = ["Station"]
     playerData["upgrades"] = ["Machine Gun"]
     playerData["cargo"] = []
     playerData.sync()

def main():
    global station
    global player
    global asteroid
    global planet
    global arena
    station = Station()
    player = Player()
    asteroid = Asteroid()
    planet = Planet()
    arena = Arena()
    player.gameOptions()

def saveSystem(): #A function that saves all the player's statistics
    playerData["credits"] = credits
    playerData["fuel"] = fuel
    playerData["hull"] = hull
    playerData["position"] = position
    playerData["upgrades"] = upgrades
    playerData["cargo"] = cargo
    playerData.sync()
    playerData.close()
    print("Data saved!\n")

######################################################################

menu()