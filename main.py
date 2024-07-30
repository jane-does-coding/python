def print_welcome_message():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious dungeon with three rooms.")
    print("Explore the rooms to find the key and escape.")
    print("Type 'look' to inspect the room, 'go [direction]' to move, and 'quit' to end the game.")

def room_description(room):
    if room == 'entrance':
        print("""
        You are at the dungeon entrance.
        There are doors to the north and east.
         _______
        |       |
        |       |
        |       |_______
        |               |
        |   ENTRANCE    |
        |_______________|
        """)
    elif room == 'hall':
        print("""
        You are in a long hall.
        There are doors to the south and east and north.
         _______________
        |               |
        |      HALL     |
        |               |
        |               |
        |_______________|
        |       |
        """)
    elif room == 'treasure':
        print("""
        You are in a treasure room!
        There's a door to the west.
         _______________
        |               |
        |   TREASURE    |
        |      ROOM     |
        |               |
        |_______________|
        """)
    elif room == 'puzzle':
        print("""
        You are in a puzzle room!
        There's a door to the west and north.
         _______________
        |               |
        |    PUZZLE     |
        |      ROOM     |
        |               |
        |_______________|
        """)
    elif room == 'exit':
        print("""
        You are at the dungeon exit.
        You need a key to escape.
         _______
        |       |
        |       |
        |   EXIT|
        |_______|
        """)

def main():
    current_room = 'entrance'
    has_key = False
    print_welcome_message()

    while True:
        room_description(current_room)
        command = input("> ").strip().lower()

        if command == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        elif command == 'look':
            if current_room == 'entrance' and not has_key:
                print("You see a shiny key in the corner.")
            elif current_room == 'puzzle' and not has_key:
                print("Solve the puzzle to get the key.")
        elif command == 'go north':
            if current_room == 'entrance':
                current_room = 'hall'
            elif current_room == 'hall':
                current_room = 'exit'
        elif command == 'go east':
            if current_room == 'entrance':
                current_room = 'puzzle'
            elif current_room == 'hall':
                current_room = 'treasure'
        elif command == 'go south':
            if current_room == 'hall':
                current_room = 'entrance'
        elif command == 'go west':
            if current_room == 'puzzle':
                current_room = 'entrance'
            elif current_room == 'treasure':
                current_room = 'hall'
        else:
            print("Invalid command. Try 'look', 'go [direction]', or 'quit'.")

        if current_room == 'exit' and has_key:
            print("Congratulations! You've found the key and escaped the dungeon!")
            break
        elif current_room == 'puzzle' and not has_key:
            print("You found the key in the puzzle room! You can now exit the dungeon.")
            has_key = True

main()
