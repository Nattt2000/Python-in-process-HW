"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Natálie Zýková
email: natalie.zykova@seznam.cz
"""


# Libraries

import random as rd
import time


# Introduction

separator = "-----------------------------------------------"

print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}""")


# Functions

def generate_secret_number() -> str:
    """
    Generates secret number.
    """
    first_digit = rd.randint(1,9)
    first_digit_str = str(first_digit)
    list_digits = []
    list_digits.append(first_digit_str)
    options_digits = list(range(0,10))
    options_digits.remove(first_digit)
    digits = rd.sample(options_digits, 3)
    for digit in digits:
        digit_str = str(digit)
        list_digits.append(digit_str)
    secret_number_str = "".join(list_digits)
    return secret_number_str


def test_duplication(attempt: str) -> str:
    """
    Controls if the digits in attempt number repeat.
    If yes then writes "wrong input".
    If not then writes "right input".
    """
    if len(attempt) == len(set(attempt)):
        output = "right input"
    else:
        output = "wrong input"
    return output


def compare_bull_cow(secret: str, attempt: str) -> dict:
    """
    Gradually compares all the digits of the secret number with the digits of the attempted number.
    If finds a match of a digit without a match of the location then writes cow.
    If finds a match of a digit together with a match of its location then writes bull.
    """
    counts_dict = {"bull": 0, "cow": 0}
    for i in range(len(secret)):
        for j in range(len(attempt)):
            if i == j and secret[i] == attempt[j]:
                counts_dict["bull"] += 1
            if i != j and secret[i] == attempt[j]:
                counts_dict["cow"] += 1
    return counts_dict


def add_s(key_1: str, key_2: str, counts_dict: dict) -> str:
    """
    Looks at values of given keys.
    If these values eaqual 0 or bigger than 1, adds letter 's' behind the keys.
    If these values eaqual 1, doesn't add anything and lets the key same.
    Saves newly gained keys to the list.
    Writes a result such as 'value_1 key_1, value_2 key_2'.
    """
    list_new_keys = []
    for key in counts_dict:
        if counts_dict[key] > 1 or counts_dict[key] == 0:
            new_key = key + "s"
            list_new_keys.append(new_key)
        else:
            new_key = key
            list_new_keys.append(new_key)
    result = f"{counts_dict[key_1]} {list_new_keys[0]}, {counts_dict[key_2]} {list_new_keys[1]}"
    return result


def run_game() -> None:
    """
    Main part of the program using all the functions above.
    First avoids the wrong inputs.
    If gets the right input, tests the attempted number.
    Gives you feedback about your attempt in form of 'X bulls, Y cows'.
    Testing until it's same as the secret number, then writes '4 bulls, 0 cows'
    Writes the number of your attempts, form of your answers and total time of guessing.
    """
    start = time.time()
    game = True
    count_attempts = 0
    list_results = []
    secret_number_str = generate_secret_number()

    while game:
        attempt_number_str = input()
        try:
            int(attempt_number_str)
        except ValueError:
            print("The input must contain only digits.")
            print(separator)
        else:
            if len(attempt_number_str) != 4:
                print("The input must contain exactly 4 digits.")
                print(separator)
            elif attempt_number_str[0] == "0":
                print("The input must not start with 0")
                print(separator)
            else:
                if test_duplication(attempt_number_str) == "wrong input":
                    print("The digits must be unique.")
                    print(separator)
                else:
                    counts_dict = compare_bull_cow(secret_number_str, attempt_number_str)
                    result = add_s("bull", "cow", counts_dict)
                    if counts_dict["bull"] == 4 and counts_dict["cow"] == 0:
                        count_attempts += 1
                        list_results.append(result)
                        if (counts_dict) == 1:
                            print(f"Correct, you've guessed the right number in {count_attempts} guess!")
                        else:
                            print(f"Correct, you've guessed the right number in {count_attempts} guesses!")
                        game = False
                    else:
                        print(result)
                        print(separator)
                        count_attempts += 1
                        list_results.append(result)
   
    end = time.time()
    your_time_sec = end - start
    your_time_min = your_time_sec // 60
    residue_sec = your_time_sec % 60

    print(f"That's amazing!")
    for i in range(count_attempts):
        print(f"game {i + 1}: {list_results[i]}")
    print(f"Your time is {your_time_min:.0f} minutes and {residue_sec:.0f} seconds.")
    print(separator)


# Call the game

run_game()