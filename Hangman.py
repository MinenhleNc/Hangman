import random

# Hangman visuals (6 wrong guesses)
hangman_stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

# Words and hints (all ≤6 letters)
stages = [
    {"word": "dog", "hint": "Stage 1: This animal barks.", "extra_hint": "Often called man's best friend."},
    {"word": "apple", "hint": "Stage 2: A common fruit.", "extra_hint": "Keeps the doctor away."},
    {"word": "tiger", "hint": "Stage 3: Big cat with stripes.", "extra_hint": "Native to Asia."},
    {"word": "chair", "hint": "Stage 4: You sit on it.", "extra_hint": "Has legs but isn’t alive."},
    {"word": "swiss", "hint": "Stage 5: A European country.", "extra_hint": "Famous for chocolate and watches."}
]

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    print("Welcome to Okuhle's Hangman!\n")
    max_wrong = 6
    
    for stage_num, stage in enumerate(stages, start=1):
        word = stage["word"].lower()
        hint = stage["hint"]
        extra_hint = stage["extra_hint"]
        guessed_letters = []
        wrong_guesses = 0
        
        print(f"\n{hint}")
        
        while wrong_guesses < max_wrong and "_" in display_word(word, guessed_letters):
            print(hangman_stages[wrong_guesses])
            print("Word:", display_word(word, guessed_letters))
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            
            guessed_letters.append(guess)
            
            if guess in word:
                print("Correct!")
            else:
                wrong_guesses += 1
                if wrong_guesses == max_wrong - 1:
                    print(f"Wrong! {wrong_guesses}/{max_wrong} wrong guesses.")
                    print("⚠️ Extra hint:", extra_hint)
                else:
                    print(f"Wrong! {wrong_guesses}/{max_wrong} wrong guesses.")
        
        if "_" not in display_word(word, guessed_letters):
            print(f"🎉 Congrats! You guessed the word '{word}' and move to the next stage! 🎉")
        else:
            print(hangman_stages[wrong_guesses])
            print(f"💀 Stage failed! The word was '{word}'. Better luck next time!")
            break
    else:
        print("\n🏆 Congratulations! You completed all stages of Okuhle's Hangman! 🏆")

# Start the game
hangman_game()
