import unittest
def split_words(txt):
    return txt.split(',') if txt.find(' ') == -1 else txt.split()