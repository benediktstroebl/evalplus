
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_char = lambda x: len(set(x))
    max_word = max(words, key=unique_char)
    if len(max_word) == unique_char(max_word):
        return max_word
    else:
        return max(words, key=lambda x: (unique_char(x), x))
