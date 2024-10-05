from Anisiann_games.engine_game import run_game
from Anisiann_games.games import lcm_game, progression_game


def main():
    print("Choose a game number:")
    print("1. Least Common Multiple")
    print("2. Geometric Progression")

    user_choice = input("Your choice: ")

    if user_choice == "1":
        run_game(lcm_game)
    elif user_choice == "2":
        run_game(progression_game)
    else:
        print("Please try again. Repeat your choice")

if __name__ == "__main__":
    main()