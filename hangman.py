import random

def hangman():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'developer', 'software', 'algorithm']
    word = random.choice(words)  # Select a random word
    guessed_word = ['_'] * len(word)  # Display the word as underscores initially
    attempts = 6  # Maximum number of incorrect guesses allowed
    guessed_letters = set()  # Keep track of guessed letters

    print("Welcome to Hangman!")
    print(f"Your word: {' '.join(guessed_word)}")
    print(f"You have {attempts} incorrect guesses allowed.")

    while attempts > 0 and '_' in guessed_word:
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            # Reveal the guessed letter in the word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts remaining.")

        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    # Check the result
    if '_' not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()