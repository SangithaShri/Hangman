import random
import words
import stickfigure


def hangman():
    chosen_word = random.choice(words.spell)
    guessed_letters = []  # List to store guessed letters
    attempts = 7  # Number of attempts allowed

    print("Welcome to Hangman!")

    while attempts > 0:

        print(stickfigure.draw_hangman(attempts))

        # Display the current state of the word
        display_word = ''
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_'

        print("Current word:", display_word)
        print("Attempts remaining:", attempts)

        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is valid
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            print("Correct guess!")

            # Check if the player has guessed all the letters
            if all(letter in guessed_letters for letter in chosen_word):
                print("Congratulations! You've guessed the word:", chosen_word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1

    else:
        print(stickfigure.draw_hangman(0))
        print("Game over! You ran out of attempts.")
        print("The word was:", chosen_word)


hangman()
