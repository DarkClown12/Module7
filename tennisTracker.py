# # Function to display the current win and loss counts
# def display_stats(wins, losses):
#     print("Current Stats:")
#     print("Wins:", wins)
#     print("Losses:", losses)

# # Function to update the win count
# def update_wins(wins):
#     wins += 1
#     return wins

# # Function to update the loss count
# def update_losses(losses):
#     losses += 1
#     return losses

# # Main function
# def main():
#     wins = 0
#     losses = 0
#     game_on = True
#     win_string = "1. Record a Win"

#     # Game loop
#     while game_on:
#         print(win_string)
#         print("2. Record a Loss")
#         print("3. Quit")
#         choice = input("Enter your choice (1-3): ")

#         if choice == "1":
#             wins = update_wins(wins)
#         elif choice == "2":
#             losses = update_losses(losses)
#         elif choice == "3":
#             game_on = False
#             print("Quitting...")
#         else:
#             print("Invalid choice!")

#         display_stats(wins, losses)
#         print()

# # Run the main function
# if __name__ == "__main__":
#     main()




# Function to display the current win and loss counts
def display_stats(wins, losses):
    print("Current Stats:")
    print("Wins:", wins)
    print("Losses:", losses)

# Function to update the win count
def update_wins(wins):
    wins += 1
    return wins

# Function to update the loss count
def update_losses(losses):
    losses += 1
    return losses

# Main function
def main():
    wins = 0
    losses = 0
    game_on = True

    # Example of an iterated list with accessed and used elements
    game_results = ["Win", "Loss", "Win", "Win", "Loss"]

    # Iterate over the game results list
    for result in game_results:
        if result == "Win":
            wins = update_wins(wins)
        elif result == "Loss":
            losses = update_losses(losses)

    display_stats(wins, losses)
    print()

    # Game loop
    while game_on:
        print("1. Record a Win")
        print("2. Record a Loss")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            wins = update_wins(wins)
        elif choice == "2":
            losses = update_losses(losses)
        elif choice == "3":
            game_on = False
            print("Quitting...")
        else:
            print("Invalid choice!")

        display_stats(wins, losses)
        print()

# Run the main function
if __name__ == "__main__":
    main()
