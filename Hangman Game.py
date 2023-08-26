import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    target_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_word(target_word, guessed_letters))
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in target_word:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
            
            if set(target_word) == set(guessed_letters):
                print("Congratulations! You guessed the word:", target_word)
                break
    
    if attempts == 0:
        print("You ran out of attempts. The word was:", target_word)

hangman()
