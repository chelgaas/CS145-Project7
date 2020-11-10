import json
import os
import time

"""
- added two rooms to adventure.py
    - bathroom
    - classroom311

Points (need 50) - FILL OUT GOOGLE FORM
- stuff - 4 pts
- help - 4 pts
- print room items - 4 pts
- take - 4 pts
- choose from JSON files - 6 pts
- drop - 4 pts
- game timer - 6 pts
- created game "athletic_complex.json" with helper function "create_equipment"
THESE WORK - 42 pts
- upload to github

"""


def main():
    # TODO: allow them to choose from multiple JSON files? DONE
    games_list = []

    for x in os.listdir():
        if x.endswith('.json'):
            games_list.append(x)

    
    for i, game in enumerate(games_list):
            print("  {}. {}".format(i+1, game))
    action = input("> ").lower().strip()
    try:
            num = int(action) - 1
            selected = games_list[num]
            game = selected
            print("...")
    except:
        print("I don't understand '{}'...".format(action))
        main()
        
    
    with open(game) as fp: #spooky_mansion or adventure
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    
    
    
    stuff = ['Cell Phone; no signal or battery...']
    
    start_time = time.time()

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        
        items_here = here['items']
        print(items_here)

        # TODO: print any available items in the room...
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        if action == "stuff":
            if len(stuff) > 0:
                print(stuff)
            else:
                print("You have nothing.")
            continue
        if action == "help":
            print_instructions()
            continue
        if action == "take":
            for x in here['items']:
                stuff.append(x)
                here['items'].clear()
            continue
        if action == "drop":
            for x, item in enumerate(stuff):
                print("  {}. {}".format(x+1, stuff))
            action = input("> ").lower().strip()
            try:
                num = int(action) - 1
                selected = stuff[num]
                here['items'].append(selected)
                del stuff[num]
                print("You dropped {}".format(selected))
            except:
                print("I don't understand '{}'...".format(action))
            continue
        if action == "search":
            print#(need to show "hidden" from json file)
            #how do i access hidden, items from json in play_game??
            continue
            
            

        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
            
        #TIMER
        timer = 0
    
    print("What you collected:")
    for x in stuff:
        print(x)
    print("")
    print("")
    print("=== GAME OVER ===")
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    game_time = minutes,':',seconds
    print('Elapsed time: ',minutes,'minutes,',seconds,'seconds')

def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        if "required_key" in exit:
            if exit["required_key"] in stuff:
                usable.append(exit)
            continue
        usable.append(exit)
    return usable

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" – Type 'help' to see the instructions again.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()