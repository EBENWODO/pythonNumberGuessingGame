from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game():
    print(logo)
    #Function to check user's guess against actual answer
    def check_answer(user_guess, actual_answer, turn):
        """Checks answer against guess, returns the number of turns remaining"""
        if user_guess > actual_answer:
            print("Too high.")
            return turn - 1
        elif user_guess < actual_answer:
            print("Too low.")
            return turn - 1
        else:
            print(f"You got it! The answer is {answer}")

    #Function to check the difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    #Choose random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(answer)

    turns = set_difficulty()

    guess =  0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
