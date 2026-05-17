import random

# ── Hangman ASCII art stages ──────────────────────────────────────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

# ── Word list ──────────────────────────────────────────────────────────────────
WORDS = ["python", "hangman", "coding", "laptop", "keyboard"]

# ── Helper functions ───────────────────────────────────────────────────────────

def choose_word():
    """Pick a random word from the list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def display_status(word, guessed_letters, wrong_guesses, max_wrong):
    """Print current game state to the console."""
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Word : {display_word(word, guessed_letters)}")
    print(f"Wrong guesses left : {max_wrong - wrong_guesses}")
    wrong_letters = [l for l in guessed_letters if l not in word]
    print(f"Incorrect letters  : {', '.join(sorted(wrong_letters)) if wrong_letters else 'None'}")
    print()


def get_guess(guessed_letters):
    """Prompt the player for a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single letter.\n")
        elif guess in guessed_letters:
            print("⚠  You already guessed that letter. Try another.\n")
        else:
            return guess


def play_game():
    """Run one full round of Hangman."""
    word            = choose_word()
    guessed_letters = set()
    max_wrong       = 6
    wrong_guesses   = 0

    print("\n" + "=" * 40)
    print("        🎮  HANGMAN GAME  🎮")
    print("=" * 40)
    print(f"The word has {len(word)} letters. Good luck!\n")

    while wrong_guesses < max_wrong:
        display_status(word, guessed_letters, wrong_guesses, max_wrong)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"🎉  Congratulations! You guessed the word: '{word.upper()}'")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"✅  Nice! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌  '{guess}' is not in the word.\n")

    # Lose condition
    print(HANGMAN_STAGES[max_wrong])
    print(f"💀  Game Over! The word was: '{word.upper()}'")


def main():
    """Entry point — supports replaying."""
    while True:
        play_game()
        print()
        again = input("Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye 👋\n")
            break
        print()


if __name__ == "__main__":
    main()
