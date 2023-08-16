# import required module
import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, path):
        self.words = []
        self.read_words(path)

    # path = "/mnt/c/Users/Couric/.vscode/Python/python-oop-practice/words.txt"

    def read_words(self, path):
        """Open file to read and print length of file."""
        with open(path, "r", encoding="utf-8") as f:
            self.words = [word.rstrip() for word in f.readlines()]
        print(f"{len(self.words)} words read")

    def random(self):
        """Return random word from file words.txt"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def read_words(self, file_path):
        with open(file_path, "r") as file:
            self.words = [
                word.strip()
                for word in file.readlines()
                if word.strip() and not word.startswith("#")
            ]
        print(f"{len(self.words)} words read")
