# your code goes here!
#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # store in lowercase for case-insensitive comparison

    def match(self, word_list):
        """Return a list of words from word_list that are anagrams of the initialized word."""
        sorted_word = sorted(self.word)
        return [w for w in word_list if sorted(w.lower()) == sorted_word]
