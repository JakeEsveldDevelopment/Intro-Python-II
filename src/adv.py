from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside cave entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Rock", "It's not very big, but it looks like it could do some damage if need be"),
                     Item("Piece of paper", "It looks like it once had some scribbles on it, but now it is far from legible")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item("Candlestick", "I wonder if this is what the butler did it with...."),
Item("Journal", "It's not very polite to read other peoples personal thoughts."),
Item("Lost Shoe", "I wonder where the owner is?"),
Item("Broken wine glass", "It looks like there was some sort of accident...")]),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[Item("Loose electrical cable", "Now that doesn't seem very safe")]),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item("I.O.U.", "It says, 'Sorry about taking all the loot, I need it for my dogs surgery.'")]),
}


# Link rooms together

room['outside cave entrance'].n_to = room['foyer']
room['foyer'].s_to = room['outside cave entrance']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']

#
# Main
#

print("Welcome to the Python Adventures!")
print("Would you like to start the game? Y/N: ")
inpStart = input()

def input1():
    print("What would you like to do?")
    print("Look around [i]")
    print("Move to another room [t]")
    print("Quit game [q]")
    inpChoice = input()
    return inpChoice.lower()

def input2():
    print("What would you like to do?")
    print("Look for items [l]")
    print("Move to another room [t]")
    print("Quit game [q]")
    inpChoice = input()
    return inpChoice.lower()

def inputLook(currentRoom: Room):
    if currentRoom.items == None:
        print("You look around, but you can't find anything of interest.")
        print("Press any key to return")
        input()
        gameloop(player, False)
    else:
        print("You take a look around and you find:")
        counter = 1
        for i in currentRoom.items:
            print(i.name + f"     [{counter}] - inspect")
            counter += 1
        print("Go back [g]")
        inpChoice = input()
        if inpChoice.lower() == "g":
            gameloop(player, False)
        else:
            try:
                print(currentRoom.items[int(inpChoice) - 1].desc)
                print("Go Back [g]")
                inpChoice = input()
                if inpChoice.lower() == "g":
                    inputLook(currentRoom)
                else:
                    print("Invalid selection. Please try again.")
                    gameloop(player, False)
            except ValueError:
                print("Invalid selection. Please try again.")
                gameloop(player, False)


def inputMove(currentRoom: Room):
    print("You look in all directions, and it seems the places you can get to from here are:")
    w_available = False
    e_available = False
    n_available = False
    s_available = False
    if currentRoom.n_to != None:
        print(currentRoom.n_to.name + " [n]")
        n_available = True
    if currentRoom.s_to != None:
        print(currentRoom.s_to.name + " [s]")
        s_available = True
    if currentRoom.e_to != None:
        print(currentRoom.e_to.name + " [e]")
        e_available = True
    if currentRoom.w_to != None:
        print(currentRoom.w_to.name + " [w]")
        w_available = True

    print("Where would you like to go?")
    inpChoice = input()
    if inpChoice.lower() == "n" and n_available == True:
        return currentRoom.n_to
    elif inpChoice.lower() == "s" and s_available == True:
        return currentRoom.s_to
    elif inpChoice.lower() == "w" and w_available == True:
        return currentRoom.w_to
    elif inpChoice.lower() == "e" and e_available == True:
        return currentRoom.e_to
    else:
        print("Invalid choice, please try again")
        gameloop(player, False)


def gameloop(player, first):
    if first == True:
        print(f"Welcome, {player.name}! to the wonderful adventures of Python!")
    
    print(f"You take a look around, and it appears that you are in the {player.currentRoom.name}")
    inpChoice = input1()

    if inpChoice == "i":
        print("You take a look around and you see....")
        print(player.currentRoom.desc)
        inpChoice = input2()
        
        if inpChoice == "t":
            inpChoice = inputMove(player.currentRoom)
            player.currentRoom = inpChoice
            gameloop(player, False)
        elif inpChoice == "q":
            print("See you soon!")
            exit()
        elif inpChoice == "l":
            inputLook(player.currentRoom)
        else:
            print("Invalid selection. Please try again.")
            gameloop(player, False)
    elif inpChoice == "t":
        inpChoice = inputMove(player.currentRoom)
        player.currentRoom = inpChoice
        gameloop(player, False)
    elif inpChoice == "q":
        print("See you soon!")
        exit()
    else:
        print("Invalid selection. Please try again.")
        gameloop(player, False)

        



# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


if(inpStart.lower() == "n"):
    print("Goodbye!")
    exit()
else:
    print("What would you like your name to be?")
    inpName = input()
    currentRoom = room["foyer"]
    player = Player(inpName, currentRoom)
    gameloop(player, True)
    
