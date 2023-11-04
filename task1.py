# coding for a hangman game in python!
import random

# List of words for the game
list_of_words = ['pasta','lasagna','cheese','pizza','polenta','noodles']

# defining a function for choosing random word
def choose_random_word():
    return random.choice(list_of_words)

# defining a function for displaying current progress
# internally loop will take turn twice one for printing dashes and second for printing the guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# defining a function for initializing the game
def hangman():
    word = choose_random_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    
    while attempts < max_attempts:
        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if word == display_word(word, guessed_letters):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()

