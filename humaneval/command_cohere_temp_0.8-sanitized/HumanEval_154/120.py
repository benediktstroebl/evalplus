import unittest
def cycpattern_check(word1, word2):
    rotated = ''.join(word2.split())
    return word1.find(rotated) != -1