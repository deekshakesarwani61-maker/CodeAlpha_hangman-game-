import random
# random module is used to randomly choose a word from a list

# List of possible words for the game
word_list = ["python", "computer", "programming", "hangman", "developer"]

# Randomly choose one word from the list
secret_word = random.choice(word_list)

# Create a list to store guessed letters (initially _ for each letter)
guessed_letters = ["_"] * len(secret_word)

# Number of wrong guesses allowed
attempts_left = 6

# List to store letters already guessed by the player
used_letters = []

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Main game loop (runs until game ends)
while attempts_left > 0 and "_" in guessed_letters:
    
    # Show current progress of the word
    print("\nWord:", " ".join(guessed_letters))
    
    # Show used letters
    print("Used letters:", " ".join(used_letters))
    
    # Show remaining attempts
    print("Attempts left:", attempts_left)
    
    # Take input from user
    guess = input("Enter a alphabet: ")
    
    # Check if input is valid (only one alphabet)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE alphabet letter.")
        continue
    
    # Check if letter was already guessed
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    
    # Add guessed letter to used letters list
    used_letters.append(guess)
    
    # Check if guessed letter is in secret word
    if guess in secret_word:
        print("Good guess!")
        
        # Reveal all positions of the guessed letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_letters[i] = guess
    else:
        print("Wrong guess!")
        attempts_left -= 1   # Reduce attempts if wrong

# Game over conditions
if "_" not in guessed_letters:
    print("\n🎉 Congratulations! You won!")
    print("The word was:", secret_word)
else:
    print("\n Game Over! You lost.")
    print("The word was:", secret_word)

