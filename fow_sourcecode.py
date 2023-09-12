import time
import random

def print_pause(*messages, delay=2):
    """
    Print messages with a delay between them.
    
    Args:
        *messages (str): The messages to be printed.
        delay (int): The delay in seconds between messages (default is 2 seconds).
    """
    for message in messages:
        print(message)
        time.sleep(delay)

def intro():
    print_pause("Welcome to the Forest of Whispers.")
    print_pause("You awaken in a dense and mysterious forest.")
    print_pause("The trees loom high above you, blocking out the sun's rays.")
    print_pause("A soft breeze rustles the leaves, and you hear distant whispers.")
    print_pause("You notice two paths ahead of you:")
    print_pause("1. A narrow, overgrown trail that seems to lead deeper into the forest.")
    print_pause("2. A well-trodden path that heads toward a distant clearing.")

def get_player_choice():
    while True:
        choice = input("Which path will you choose? (1/2): ")
        
        if choice == '1' or choice == '2':
            return choice
        else:
            print_pause("Invalid choice. Please enter '1' or '2'.")

def forest_game():
    intro()
    choice = get_player_choice()
    
    if choice == '1':
        print_pause("You venture down the overgrown trail, feeling a sense of foreboding.")
        encounter = random.choice(['monster', 'mysterious figure'])
        
        if encounter == 'monster':
            print_pause("Suddenly, a fearsome monster emerges from the shadows!")
            print_pause("You must fight to defend yourself.")
            # Implement combat logic here
            # Depending on the outcome, you can determine a win or loss condition.
        else:
            print_pause("As you continue along the trail, you encounter a mysterious figure.")
            print_pause("They offer you a riddle.")
            # Implement a riddle or puzzle here
            # Depending on the player's answer, you can determine a win or loss condition.
        
    elif choice == '2':
        print_pause("You follow the well-trodden path to the clearing.")
        print_pause("In the clearing, you find a treasure chest.")
        print_pause("Do you open the chest or leave it untouched?")
        chest_choice = get_player_choice()
        
        if chest_choice == '1':
            print_pause("You open the chest and find valuable treasures!")
            # Implement a win condition
        else:
            print_pause("You decide to leave the chest untouched and continue exploring.")
            # Implement other game events

# Start the game
forest_game()
