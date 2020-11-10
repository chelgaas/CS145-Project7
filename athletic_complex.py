import json

# This global dictionary stores the name of the room as the key and the dictionary describing the room as the value.
GAME = {
    '__metadata__': {
        'title': 'Athletic Complex',
        'start': 'FrontDesk'
    }
}

def create_room(name, description, ends_game=False, first_time=None):
    assert (name not in GAME)
    room = {
        'name': name,
        'description': description,
        'exits': [],
        'items': [],
    }
    # Is there a special message for the first visit?
    if first_time:
        exit['first_time'] = first_time
    # Does this end the game?
    if ends_game:
        room['ends_game'] = ends_game

    # Stick it into our big dictionary of all the rooms.
    GAME[name] = room
    return room

def create_equipment(name, description, location):
    assert (name not in GAME)
    room = {
        'name': name,
        'location':location,
        'description': description,
        'exits': [],
        'items': [],
    }

    # Stick it into our big dictionary of all the rooms.
    GAME[name] = room
    create_exit(location, name, description) #access to equipment
    create_exit(name, location, "Finish your set.") #back to location
    return room



def create_exit(source, destination, description, required_key=None, hidden=False):
    # Make sure source is our room!
    if isinstance(source, str):
        source = GAME[source]
    # Make sure destination is a room-name!
    if isinstance(destination, dict):
        destination = destination['name']
    # Create the "exit":
    exit = {
        'destination': destination,
        'description': description
    }
    # Is it locked?
    if required_key:
        exit['required_key'] = required_key
    # Do we need to search for this?
    if hidden:
        exit['hidden'] = hidden
    source['exits'].append(exit)
    return exit

FrontDesk = create_room("FrontDesk", """You are standing at the front desk of the Athletic Complex.
You need to get out.""")
create_exit(FrontDesk, "LockerRoom", 'There is a door labeled "Locker Room"')
create_exit(FrontDesk, "Outside", "The front door. You need to swipe your student ID", "Student ID")

Outside = create_room("Outside", "You've escaped, but did you leave bigger than you came?", ends_game = True)

LockerRoom = create_room("LockerRoom", "You are standing in a locker room.")
LockerRoom["items"].append("Student ID")
create_exit(LockerRoom, "FrontDesk", "Return the the front desk area.")
create_exit(LockerRoom, "Hallway", "Go through a blue door next to the showers.")

Hallway = create_room("Hallway", """You are standing in a hallway filled with hall-of-fame portraits.
There is no photo of you... yet.""")
create_exit(Hallway, "LockerRoom", "Go through a blue door.")
create_exit(Hallway, "WeightRoom", "Go down some stairs.")

WeightRoom = create_room("WeightRoom", """You are standing in the the Iron Cathedral.
This is hallowed ground.""")
create_exit(WeightRoom, "Hallway", "Go up the stairs.")
BenchPress = create_equipment("BenchPress", "A bench press loaded with 85% of your max. Who forgot to rerack their weights?", WeightRoom)
BenchPress['items'].append("Huge Chest Gains")
SquatRack = create_equipment("SquatRack", "Uh oh––a squat rack––is today leg day?", WeightRoom)
SquatRack['items'].append("Massive Quads")
Deadlift = create_equipment("Deadlift", "Just a bar on the ground loaded up with four wagon wheels. Who's gonna pick it up?", WeightRoom)
Deadlift['items'].append("Juicy Hamstrings")
Deadlift['items'].append("Instagram Views")
LatPulldown = create_equipment("LatPulldown", "It's a lat pulldown machine. You don't usually train back but there's a mirror...", WeightRoom)
LatPulldown['items'].append("Yoked Back")
LatPulldown['items'].append("Free Bicep Pump")
CableMachine = create_equipment("CableMachine", "Do some tricep extensions. Why not?", WeightRoom)
CableMachine['items'].append("Steezed Tris")
CalfMachine = create_equipment("CalfMachine", "Try some seated calf raises. Need to maintain a balanced physique.", WeightRoom)
CalfMachine['items'].append("The knowledge that your calves will never grow :(")



##
# Save our text-adventure to a file:
##
with open('athletic_complex.json', 'w') as out:
    json.dump(GAME, out, indent=2)


