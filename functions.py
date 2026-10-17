from rich import print


def welcome_message() -> str:
    return """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""


def get_difficulty_level() -> int:
    dificultes = ["Easy", "Medium", "Hard"]

    while True:
        try:
            level = int(input("Enter your choice: "))
            if level in [1, 2, 3]:
                print(
                    f"\nGreat! You have selected the {dificultes[level - 1]} difficulty level.\nLet's start the game!\n"
                )
                return level
            else:
                print("\n[red]Invalid input. Please enter 1, 2, or 3.[/red]\n")
        except ValueError:
            print("\n[red]Invalid input. Please enter a number (1, 2, or 3).[/red]\n")
