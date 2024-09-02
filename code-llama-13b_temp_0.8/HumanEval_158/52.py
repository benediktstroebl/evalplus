
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_char(word):
        """Returns a dictionary of unique charcters in the word
        and their frequency"""
        return {c: word.count(c) for c in word}

    def get_max(words):
        """Returns the word with maximum frequency of unique characters"""
        return max(words, key=lambda x: len(count_char(x)))

    return get_max(words)















