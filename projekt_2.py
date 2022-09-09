"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Silvie Bartošíková
email: silviebartosikova@gmail.com
discord: Silvie B.#8828
"""

import time
import random

"""
A user in this game is challenged to guess a 4-digit secret number generated 
by the program. There are 30 attempts for the player to discover it.
Generated number contains numerals 0-9. Each digit is used only once so 1230 
is acceptable but 1102 is not. The number cannot begin with a zero.
The program counts "bulls" and "cows" for each user's guess. If the digit is 
in the right position it is a bull. If the digit exists in generated number but 
it is at incorrect position it is a cow.
The game ends either by running out of attempts (loss) or by user giving 
a correct guess. The application calculates user's wins, losses and time that
it took to guess the number.
"""

# Auxiliary variables
separator = len(f"Correct, you've guessed the right number in 4 guesses!") * "-"


# Greetings to the user
def welcome():
    print(f"Hi there!",
          separator,
          f"I've generated a random 4 digit number for you.",
          f"Let's play a Bulls and Cows game.",
          separator,
          sep="\n")


# Generate a random 4 digit number
def generate():
    generate_num = str(random.randint(1000, 10000))
    while not check_unique_digits(generate_num):
        generate_num = str(random.randint(1000, 10000))
    return generate_num


# Verify that no digits are repeated
def check_unique_digits(number):
    for i in number:
        if number.count(i) > 1:
            return False
    return True


# Choose a 4 digit number
def guess():
    guess_num = input("Please enter your guess: ")
    while not validate_guess(guess_num):
        guess_num = input("Please enter your guess: ")
    return guess_num


# If the number was entered correctly, return True.
def validate_guess(guess_num):
    if len(guess_num) != 4:
        print("You must enter in exactly 4 digits.")
        return False
    if not guess_num.isdigit():
        print("You must only enter numbers.")
        return False
    if guess_num[0] == "0":
        print("Your four-digit number must not start with a zero.")
        return False
    if not check_unique_digits(guess_num):
        print("You are not allowed to repeat digits.")
        return False
    return True


# Count bulls and cows
def bulls_and_cows(generate_num, guess_num):
    counter_bulls = 0
    counter_cows = 0
    for i in range(4):
        if generate_num[i] == guess_num[i]:
            counter_bulls += 1
    for i in range(4):
        for j in range(4):
            if generate_num[i] == guess_num[j]:
                counter_cows += 1
    return counter_bulls, counter_cows - counter_bulls


# Determine singular and plural number for "cow/s" and "bull/s"
def result_count(name, count):
    return (name + "s" if count > 1 else name) + ": " + str(count)


# A single game play
def game():
    attempts = 1
    start_time = time.time()
    generate_num = generate()
    guess_num = "1000"

    while (attempts <= 30) and (generate_num != guess_num):
        print("Attempt number: ", attempts)
        guess_num = guess()
        result = (bulls_and_cows(generate_num, guess_num))
        print(result_count("Bull", result[0]), "and",
              result_count("Cow", result[1]))
        print(separator)
        attempts += 1
    if attempts <= 30:
        print(f"Correct, you've guessed the right number in 4 guesses!")
        finish_timer(start_time, True)
        return True
    else:
        print(f"Unfortunately, you didn't guess, ",
              f"there was a hidden number {generate_num}",
              sep="\n")
        finish_timer(start_time, False)
        return False


# Game statistics
# A question about continuing and ending the game
def play():
    wins_count = 0
    losses_count = 0
    again = "y"
    while again.lower() == "y":
        if game():
            wins_count += 1
        else:
            losses_count += 1
        print(f"Number of wins: {wins_count}",
              f"Number of losses: {losses_count}",
              separator,
              sep="\n")
        again = input("Would you like to play again? (y/n): ")
    print()
    print("Bye!")


# Game timer
def finish_timer(start_time, win):
    end_time = time.time()
    print(separator)
    duration = int(end_time - start_time)
    if duration <= 99 and win:
        print(f"Wow! You guessed the number in {duration} SECONDS!",
              f"Your time is incredible!",
              separator,
              sep="\n")
    elif duration <= 150 and win:
        print(f"Great, {duration} SECONDS it's not a bad time at all.",
              separator,
              sep="\n")
    elif duration >= 151 and win:
        print(f"{duration} SECONDS! Congratulations,",
              f"but you still have place to improve.",
              separator,
              sep="\n")


welcome()
play()
