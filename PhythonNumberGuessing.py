#Python number guessing game
import random

high=100
low=1
guesses=0

answer=random.randint(low,high)
is_running=True
print("PYTHON NUMBER GUESSING GAME")
print(f"Guess between {low}-{high}")
while is_running:

    guess=input("Enter your guess: ")
    guesses+=1
    if guess.isdigit():
        guess=int(guess)
        if guess<low and guess>high :
            print("your guess is out of range")
        elif guess<answer:
            print("guess is low")
        elif guess>answer:
            print("guess is high")
        else:
            print(f"correct answer is {answer}")
            break
    else:
        print("invalid guess")
        print(f"please Guess between {low}-{high}")

print(f"it took you {guesses} !!!")