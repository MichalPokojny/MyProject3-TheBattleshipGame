from random import randint


class Game_board:
    """
    Main class game
    """
    def __init__(self, size, num_ships):
        """
        Set attribute for size and number of ships.
        Set board for the game.
        """
        self.size = size
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)]

    def populate_board(self, size, num_ships):
        # Function to populate the board with random locations. 
        
        for i in range(num_ships):
            self.x, self.y = randint(0, size - 1), randint(0, size - 1)
            self.board[self.x][self.y] = "@"

            return self.board[self.x][self.y]

    def print_board(self):
        # Function to print the board with location of the ship

        print("    0 1 2 3 4")
        row_number = 0
        for row in self.board:
            print("  ", row_number, " ".join(row))
            row_number += 1

    def make_guess(self):
        """
        Function for asking the location from the user
        then run the try, exept methods to catch error for invalid 
        inputs.
        """
        try:
            x = input("Enter row number which you want to target.")
            while x not in '01234' or x == "":
                print("Not valid number for a row, please choose again.\n")
                x = input("Enter row number which you want to target.")

            y = input("Enter column number which you want to target.")
            while y not in '01234' or y == "":
                print("Not a valid number for a column, please choose again.")
                y = input("Enter column number which you want to target.")

            return int(x), int(y)
        except ValueError:
            print("Not a valid input.Try again.\n")
            return self.make_guess()        


def New_game():
    # Main function to play the game
    print("---------------------------------------------------------------")
    name = input("Hi! What's your name?\n")
    print(f"\nWelcome {name} to the Ultimate Battleship game!")
    
    print("\nThis game is for those who like to play a real quick game,\n\
you have only 3 guesses to get the location of the ship to try to sink it.")
    print("You need to select row and column from 0 to 4 only.")
    print("Good luck!\n")
    print("---------------------------------------------------------------")

    size = 5
    num_ships = 1

    game_board = Game_board(size, num_ships)    
    
    game_board.populate_board(size, num_ships)
    
    tries = 3
    hits = 0
    for _ in range(3):
        x, y = Game_board.make_guess(object)

        if game_board.board[x][y] == "@":
            print(f"\nHit! Well done {name}. You won!")
            break
            hits += 1
            tries -= 1

        else:
            print("Miss! Try again!")
            print(f"You have {tries - 1} tries left.")
            tries -= 1
            print("-------------------------------------------------------------")

    if tries == 0:
        print("Sorry you lost")
        print(f"\nMiss! Bad luck {name}, hopefully you can get it next time!")
        print("Have a look where the ship was located!")
        game_board.print_board()
    

New_game()