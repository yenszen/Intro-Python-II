from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# declare all the items

items = {
    'football': Item("football", "Something to kick"),
    'basketball': Item("basketball", "Something to throw"),
    'golfball': Item("golfball", "Something to hit"),
    'gumball': Item('gumball', "Something to eat"),
    'stressball': Item('stressball', 'Something to squeeze')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# assign items to rooms
room["outside"].add_item(items["football"])
room["foyer"].add_item(items["basketball"])
room["overlook"].add_item(items["golfball"])
room["narrow"].add_item(items["gumball"])
room["treasure"].add_item(items["stressball"])

# directional function


def directional(action):
    if action == "n":
        try:
            player1.current_room = player1.current_room.n_to
        except AttributeError:
            print("This leads nowhere, please choose again")
    elif action == "e":
        try:
            player1.current_room = player1.current_room.e_to
        except AttributeError:
            print("This leads nowhere, please choose again")
    elif action == "s":
        try:
            player1.current_room = player1.current_room.s_to
        except AttributeError:
            print("This leads nowhere, please choose again")
    elif action == "w":
        try:
            player1.current_room = player1.current_room.w_to
        except AttributeError:
            print("This leads nowhere, please choose again")

# Make a new player object that is currently in the 'outside' room.


input1 = input("What is your name?\n")

player1 = Player(str(input1))
player1.current_room = room["outside"]

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

playing = True

while playing == True:
    print(f"You are currently in {player1.current_room.name}\n")
    print(f"{player1.current_room.description}\n")

    current_room_items = []

    for item in player1.current_room.items:
        current_room_items.append(item.name)

    if len(current_room_items) != 0:
        print(f"This room contains: {current_room_items}\n")
    else:
        print("There are no more items in this room")

    print("Next action?\n")
    print("1. Type 'get [item_name]' to collect each item")
    print(
        "2. n = [north] s = [south] e = [east] w = [west]' to move to another room")
    print("3. Type i to view your inventory")
    print("4. Type q to quit\n")
    print("*****************************************\n")

    action = str(input()).lower()

    if action == "q":
        playing = False

    elif action == "n" or action == "e" or action == "s" or action == "w":
        directional(action)

    elif action.startswith("get"):
        item_name = items[action.split()[1]]

        if item_name in player1.current_room.items:
            player1.add_item(item_name)
            player1.current_room.drop_item(item_name)
            item_name.on_take()
        else:
            print("No such item in the room!")

    elif action.startswith("drop"):
        item_name = items[action.split()[1]]

        if item_name in player1.inventory:
            player1.drop_item(item_name)
            player1.current_room.add_item(item_name)
        else:
            print("No such item in your inventory!")

    elif action == "i":
        inventory = []
        for i in player1.inventory:
            inventory.append(i.name)
        print(f"You have {inventory}")
