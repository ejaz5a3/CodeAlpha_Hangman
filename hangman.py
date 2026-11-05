import random

words = ["python", "program", "keyboard", "computer", "internet"]

secret_word = random.choice(words)

guessed_letters = []      
wrong_guesses = 0         
max_wrong = 6             

print("=== Welcome to Hangman! ===")
print(f"Guess the word. You can make {max_wrong} wrong guesses.\n")

while wrong_guesses < max_wrong:

    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong! Wrong guesses left: {max_wrong - wrong_guesses}")

    print("Guessed so far:", ", ".join(guessed_letters))
    print()

else:
    print("\n💀 Game Over! The word was:", secret_word)