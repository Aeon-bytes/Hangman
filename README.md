# Hangman Game

A command-line Hangman word-guessing game built in Python. The game dynamically fetches random words from an online API for a fresh experience in every round!

## Features
- **Dynamic Words**: Automatically retrieves random secret words using the [Random Word API](https://random-word-api.herokuapp.com/).
- **Classic Gameplay Mechanics**: Start with **7 chances** to guess the hidden word.
- **Real-Time Visual Feedback**: Displays letter reveals and masked word status (`_ _ _`) after every guess.

## Prerequisites
- Python 3.6+
- [`requests`](https://pypi.org/project/requests/) package

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Aeon-bytes/python-hangman.git
cd python-hangman
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Run the Game
```bash
python HANGMAN.py
```

## How to Play
1. When launched, a secret word is generated and hidden behind underscores (`_`).
2. You begin with **7 chances**.
3. At the prompt (`enter a letter:`), type a letter you think is in the word.
4. **Correct Guess**: The letter fills in its position(s) and your remaining chances stay the same.
5. **Wrong Guess**: You lose 1 chance and receive an updated attempt count.
6. **Victory**: Uncover all letters in the word before running out of attempts!
7. **Defeat**: If your chances reach 0, the game reveals the correct answer.

---
