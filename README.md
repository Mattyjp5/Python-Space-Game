# Python-Project Overview

I have created a text-based space adventure and exploration game inspired by the game Elite (1984)

The aim of the game is to earn 10,000 credits to pay off a debt the player has

GitHub Repository Link:
https://olympuss.ntu.ac.uk/N1189530/Python-Project

# Initialisation 

Players are able to choose between 3 save slots

Error handling is included so that players will not need to manually create a file if it does not exist

Save data is stored in a data file and saves the player’s cargo, credits, upgrades, fuel, hull, and position 

# Modules 

* The pickle and shelf modules are imported to allow for saving and loading
* The random modules are imported to allow for randomly generated rewards
 

# Gameplay 

* The Station
  * The Station serves as the player's home base
  * The player can repair and replenish their fuel
  * The player can buy upgrades to increase their combat power
  * The player can sell materials for credits
  * The player can pay off their debt once they have 10,000 credits

## Players are able to choose between a variety of activities to obtain credits: 

* Mining 
  * Players can mine an asteroid for the chance to get different materials
  * Players can store these materials in their cargo and sell them at the Station
  * Players can mine the asteroid as much as they like, however, each mining attempt will part of the player's fuel which has to be replenished at the Station
  * Mining is the most reliable form of earning money but will most likely yield the least amount of credits

* Combat 
  * Players are able to purchase upgrades with credits, which increases their combat power statistic
  * Combat power is used to determine whether a player will be successful in combat engagements
  * Players can encounter enemies at the arena whose combat power is similar to the player's but can be from 0.5x to 3.5x stronger/weaker depending on random chance
  * Players have the option whether to proceed with the encounter or run
  * If the player chooses to continue with the encounter, the player and the enemy will take turns dealing damage (which reduces each other's combat power) until someone's combat power is depleted
  * If the player wins the engagement, the player will receive double the enemy's initial combat power in credits and will receive a small amount of hull damage
  * If the player loses the engagement, the player will lose half the enemy's initial combat power in credits and a larger amount of hull damage 
  * Random chance is used to determine how much damage the player and enemy does
  * Combat is the riskiest activity but also can offer the most credits

* Exploration 
  * Players can explore a planet for the chance to find different materials
  * Players can find fuel, diamonds and treasure (credits)
  * Random chance is used to determine the rewards the player gets from exploration
  * Exploring the planet costs more fuel than mining but offers more rewards

# Technical Overview

* I have used classes and there are 5 different classes such as:
  * The Player
  * The Station
  * The Asteroid
  * The Planet
  * The Arena

* I have used different container types such as:
  * A dictionary to allow the player to buy different upgrades and sell different materials
  * A list to keep track of what materials the player has in their cargo
  * Shelves to save and load all of the player's statistics

* I have a text-based user interface to allow the player to select which activities they'd like to do

* I have used loops to save me from duplicating code and to ensure that the player remains in the game environment

* I have used files (data files specifically) and shelves to save and load the player's data

* I have used functions to save me from duplicating code and to allow the player to go back and forth to and from different activities

# Program Flow Chart

https://imgur.com/a/b0B9iEI

# Critique

Overall, I believe that my project is quite successful. Although fairly simple, I have managed to include a wide range of programming constructs such as loops, containers, functions, classes and file management. I set out with a clear vision in mind and I managed to achieve most of what I wanted to. My saving and loading feature works quite well as I'm able to save a wide range of player statistics and different data types (strings, lists and integers) and then load them the next time the program is run. 

It was my first time using classes in a project so I was initially unsure how to use them. I believe that I've used my classes in quite a simple manner though they do what I need them to do. However, I believe that next time I should be more ambitious with my classes by using multiple of each type (and therefore using constructors), using templates and creating children. I believe that this will help me to create programs that are larger in scale and it will help to keep my future games interesting. Whilst my game is fully functional, I don't think that it is very interesting and gets boring quite quickly. Therefore, using classes more effectively will help to add more variety to my future programs and make them more enjoyable overall. 

# References

Dawson, M., 2011. *Python Programming for the Absolute Beginner* [online]. United States of America: Course Technology. Available at: https://ebookcentral.proquest.com/lib/ntuuk/reader.action?docID=3136274 [Accessed 01/12/2023]
