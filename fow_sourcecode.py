import time
import random

# Define variables to track game state
found_treasure = False

# Define a function to print messages with a delay between them.
def print_pause(message, delay = 2):
    print(message)
    time.sleep(delay)

# Define the introduction of the game.
def intro():
    print_pause("Welcome to the Forest of Whispers.")
    print_pause("You awaken in a dense and mysterious forest.")
    print_pause("The trees loom high above you, blocking out the sun's rays.")
    print_pause("you hear distant whispers.")
    print_pause("You notice two paths ahead of you:")
    print_pause("1. Take the narrow, overgrown trail.")
    print_pause("2. Follow the well trodden path to the clearing.")

# Define a function to get the player's choice and validate it.
def get_player_choice():
    while True:
        choice = input("Enter 1 to take the trail or 2 for the clearing: ")

        if choice == '1':
            return '1'
        elif choice == '2':
            return '2'
        else:
            print_pause("Invalid choice. Please enter '1' or '2'.")

# Define the main game function.
def forest_game():
    global found_treasure  # Declare a global variable

    intro()

    while True:
        choice = get_player_choice()

        if choice == '1':
            print_pause("You go down the trail, feeling a sense of unease.")
            encounter = random.choice(['monster', 'mysterious figure'])

            if encounter == 'monster':
                print_pause("Suddenly, a monster emerges from the shadows!")
                print_pause("You must fight to defend yourself.")

                # Implement combat logic here
                if player_wins_battle():
                    print_pause("You won! Now, continue your journey.")
                else:
                    print_pause("You died! You lose the game.")
                    break
            else:
                print_pause("As you go down trail, you meet a strange figure.")
                print_pause("They offer you a riddle.")

                # Implement a riddle or puzzle here
                if player_solves_riddle():
                    print_pause("You solved it and continue your journey.")
                else:
                    print_pause("You failed! You lose the game.")
                    break

        elif choice == '2':
            print_pause("You follow the well trodden path to the clearing.")
            print_pause("In the clearing, you find a treasure chest.")
            print_pause("Do you open the chest (1) or leave it untouched (2)?")
            chest_choice = input("Enter 1 to open the chest or 2 to not: ")

            if chest_choice == '1':
                found_treasure = True  # Player found the treasure
                print_pause("You open the chest and find valuable treasures!")
                if found_treasure:
                    print_pause("Congratulations! You have won the game.")

            elif chest_choice == '2':
                print_pause("You leave the chest and continue going.")

            else:
                print_pause("Invalid choice. Please enter '1' or '2'.")

        play_again = input("Would you like to play again? (y / n): ")
        if play_again.lower() != 'y':
            break

# Implement a function to check if the player wins a battle.
def player_wins_battle():
    return random.choice([True, False])  # For demonstration purposes

# Implement a function to check if the player solves a riddle.
def player_solves_riddle():
    return random.choice([True, False])  # For demonstration purposes

if __name__ == "__main__":
    forest_game()