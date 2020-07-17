from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
dictionary = {}

def traversal(room, visited=None):
    exits = room.get_exits() 
    if room.id in dictionary: #base case
        if len(exits) == len(dictionary[room.id]): 
            if room.id in visited:
                return
    if visited == None: #create set
        visited = set()
    visited.add(room.id) #add room to set
    if room.id not in dictionary: 
        dictionary[room.id] = {}
    for ext in exits: 
        if player.current_room.get_room_in_direction(ext).id not in visited:
            if ext not in dictionary[room.id]:
                player.travel(ext)
                traversal_path.append(ext)
                if len(player.current_room.get_exits()) == 1:
                    visited.add(player.current_room.id)
            if player.current_room.id not in visited:
                traversal(player.current_room, visited)
            direction = ""
            if ext == "n":
                direction = "s"
            if ext == "s":
                direction = "n"
            if ext == "w":
                direction = "e"
            if ext == "e":
                direction = "w"
            if player.current_room.id not in dictionary:
                dictionary[player.current_room.id] = {}
            if direction not in dictionary[player.current_room.id]:
                dictionary[player.current_room.id][direction] = room.id
            player.travel(direction)
            traversal_path.append(direction)

player.current_room = world.starting_room

traversal(player.current_room)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
