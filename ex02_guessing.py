import sys
import random

def random_number(min, max):
    return random.randint(min, max)

def start_game(min, max) -> None:
    print("*** Start game ***")
    print("Guess what number I am thinking of between " + str(min) + " and " + str(max))

    # Game state
    game_state = True

    # First init hidden number
    hidden_number = random_number(min, max)

    while(game_state):
        # Guess Number
        guess = int(input(">> "))

        # Logic
        if guess > hidden_number:
            c = print("Lower! What is the number?")
        elif guess < hidden_number:
            c = print("Higher! What is the number?")
        else:
            print( "Well done! You found the number, that was good " + str(hidden_number))

            # Exit Game
            game_state = False

        
if __name__ == "__main__":
    try:
        # Get all arguments
        min_string_range = sys.argv[1]
        max_string_range = sys.argv[2]
        
        if not min_string_range.isnumeric() or not max_string_range.isnumeric():
            sys.exit("The borders must be whole numbers")

        # Cast string to integer
        min_range = int(min_string_range)
        max_range = int(max_string_range)

        # Start game
        start_game(min_range, max_range)
        
    except IndexError:
        sys.exit("Two arguments required. The min and max bounds")