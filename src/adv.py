from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside cave entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
    print("Move to another room [t]")
    print("Quit game [q]")
    inpChoice = input()
    return inpChoice.lower()

def inputMove(currentRoom):
    print("You look in all directions, and it seems the places you can get to from here are:")
    w_available = False
    e_available = False
    n_available = False
    s_available = False
    if currentRoom.n_to != None:
        print(currentRoom.n_to.name + "[n]")
        n_available = True
    if currentRoom.s_to != None:
        print(currentRoom.s_to.name + "[s]")
        s_available = True
    if currentRoom.e_to != None:
        print(currentRoom.e_to.name + "[e]")
        e_available = True
    if currentRoom.w_to != None:
        print(currentRoom.w_to.name + "[w]")
        w_available = True


def gameloop(player, first):
    if first == True:
        print(f"Welcome, {player.name}! to the wonderful adventures of Python!")
        first = False
    
    print(f"You take a look around, and it appears that you are in the {player.currentRoom.name}")
    inpChoice = input1()

    if inpChoice == "i":
        print("You take a look around and you see....")
        print(player.currentRoom.desc)
        inpChoice = input2()
        
        if inpChoice == "t":
            inputMove(player.currentRoom)

        



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
    
