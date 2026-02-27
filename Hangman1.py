import random

words = ["python", "coding", "hangman", "program", "developer","maharashtra","javascript","programming"]
chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman Game")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in display:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Game Over! The word was:", chosen_word)
