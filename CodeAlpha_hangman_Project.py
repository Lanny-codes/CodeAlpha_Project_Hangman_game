word_list = ["Anxiety", "Corrupt", "Stairs", "Pride", "Excitement"]
guesses = []
Attempts = 6

# Displays characters slower
for char in "Welcome to the Hangman Game":
    print(char, end='', flush=True)
    for i in range(100000): pass
print()

print("_" * 40)
username = input("Input name: ")
print(f"welcome {username}😏")
print("_" * 40)

for char in ("Hangman is a word guessing game designed to test your intellect based on a few riddles "
             "\n Think you're up for the task??"):
    print(char, end='', flush=True)
    for i in range(100000): pass
print()

response = input("Y/N \n ")

if response == "Y"or"y":
    for char in "okay. Lets Play Hangman🤩!!!!":
        print(char, end='', flush=True)
        for i in range(100000): pass
    print()
else:
    print("Bye then.\n Sorry to see you go😭")

# Start the guessing game — go through each word in order
for word in word_list:
    guesses = []
    Attempts = 6
    chosen_word = word.upper()

    # Riddle based on word
    if chosen_word == "ANXIETY":
        riddle = "You feel me when thoughts race like fire,\nInvisible weight, yet pulling you entire."
    elif chosen_word == "CORRUPT":
        riddle = "Power has taken my soul away,\nI'm broken, dirty, led astray."
    elif chosen_word == "STAIRS":
        riddle = "Step by step you rise or fall,\nMiss one beat, and down you crawl."
    elif chosen_word == "PRIDE":
        riddle = "I lift your chin and swell your chest,\nBut unchecked, I ruin the best."
    elif chosen_word == "EXCITEMENT":
        riddle = "Heartbeats fast and eyes so wide,\nI come with joy you cannot hide."
    else:
        riddle = "A mystery word awaits you🤯."

    # Show the riddle
    for char in "Here's your riddle:\n" + riddle:
        print(char, end='', flush=True)
        for i in range(100000): pass
    print()

    # Start guessing loop
    while Attempts > 0:
        display_word = ""
        for letter in chosen_word:
            if letter in guesses:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        if "_" not in display_word:
            print("🎉 Congrats! You guessed the word:",chosen_word)
            break

        guess = input("😊Guess a letter: ").upper()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.append(guess)

        if guess in chosen_word:
            print("Correct guess!😁")
        else:
            Attempts -= 1
            print("Wrong guess. 😒Attempts left:", Attempts)

    if Attempts == 0:
        print("💀 Game Over! The word was:", chosen_word)
        break  # Stop the game if user fails a word

print("\nThanks for playing Hangman!")
