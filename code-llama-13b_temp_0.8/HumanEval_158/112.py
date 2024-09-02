
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def max_word(a, b):
        if len(a) > len(b):
            return a
        elif len(a) < len(b):
            return b
        elif a < b:
            return b
        else:
            return a

    return reduce(max_word, words)

