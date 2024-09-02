
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    maxlen = 0
    max_word = ""
    for word in words:
        current_len = len(set(word))
        if current_len > maxlen:
            maxlen = current_len
            max_word = word
    return max_word

import unittest
