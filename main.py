import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
user_choice = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

'''list of numbers to pick'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

'''Random choice'''
rand_choice = random.choice(numbers)

'''Attempts'''
attempts_easy = 10
attempts_hard = 5

'''difference between numbers'''
def difference():
    if guess > rand_choice:
        return "Too high."
    elif guess < rand_choice:
        return "Too low."
    elif guess == rand_choice:
        return f"You got it! The answer is {rand_choice}"

    return None

'''Decision for easy or hard'''
if user_choice == "easy":
    while attempts_easy > 0:
        print(f"You have {attempts_easy} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(difference())
        if guess == rand_choice:
            break
        attempts_easy -= 1

        if attempts_easy == 0 and guess != rand_choice:
            print("You've run out of guesses. You Lose!")

elif user_choice == "hard":
    while attempts_hard > 0:
        print(f"You have {attempts_hard} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(difference())
        if guess == rand_choice:
            break
        attempts_hard -= 1

        if attempts_hard == 0 and guess != rand_choice:
            print("You've run out of guesses. You Lose!")

else:
    print("Invalid input")