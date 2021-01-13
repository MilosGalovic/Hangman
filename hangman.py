import random

class Hangman:
    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.word = None
        self.result = None
        self.tries = 8
        self.letters = set()
        self.letter = None

    def correct_word(self):
        self.word = random.choice(self.words)
        self.result = "-" * len(self.word)

    def update_result(self):
        self.result = "".join([letter if letter in self.letters else "-" for letter in self.word])

    def input_check(self):
        self.letter = input("Input a letter: ")
        if len(self.letter) == 1:
            if self.letter.islower() and self.letter.isalpha():
                if self.letter not in self.letters:
                    self.letters.add(self.letter)
                    if self.letter in self.word:
                        self.update_result()
                    else:
                        print("That letter doesn't appear in the word")
                        self.tries -= 1
                else:
                    print("You've already guessed this letter")

            else:
                print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")

    def play(self):
        self.correct_word()
        print("H A N G M A N")
        while self.tries > 0:
            print("\n" + self.result)
            if "-" in self.result:
                self.input_check()
            else:
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You lost!")

    def main_menu(self):
        while True:
            self.menu = input("Type \"play\" to play the game, \"exit\" to quit: ").lower()
            if self.menu == "play":
                self.play()
            elif self.menu == "exit":
                exit()

game = Hangman()
game.main_menu()