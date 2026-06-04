import random

# 5 predefined words
words = ["python", "apple", "computer", "school", "mobile"]

# Random word choose
word = random.choice(words)

# Empty list for guessed letters
guessed_letters = []

# Wrong guesses limit
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong:

    display_word = ""

    # Show guessed letters





    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check input
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong Guess!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The word was:", word)
