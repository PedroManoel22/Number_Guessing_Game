from functions import get_difficulty_level, welcome_message


def main():
    message = welcome_message()
    print(message)

    get_difficulty_level()


if __name__ == "__main__":
    main()
