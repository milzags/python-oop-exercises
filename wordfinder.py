"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, filepath):
        """ read a file and show number of lines read """
        words_from_file = open(filepath, 'r')
        self.wordscount = 0
        self.wordslist = words_from_file.readlines()
        for line in self.wordslist: self.wordscount += 1
        print(f"{self.wordscount} words read")

    def create_list(self, words_from_file):
        """ create a list of words after reading the file"""
        wordslist = [word for word in words_from_file.readlines()]
        return wordslist

    def random_word(self):
        """ return a random word"""
        rand_word = random.choice(self.wordslist)
        return rand_word

wf = WordFinder('words.txt') 
rando_word = wf.random_word()
print(rando_word)


class RandomWordFinter(WordFinder):
    """ new randomWOrdFiner requirement: some lines will be blank
    and other lines will start with #; write code to handle this
    and re-use as much code as possible from earlier """
    

