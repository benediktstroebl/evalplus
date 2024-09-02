
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_unique = len(max(words, key = lambda x: len(set(x))))
    max_unique_word = min(words, key = lambda x: len(set(x)))
    for word in words:
        if len(set(word)) == max_unique:
            return word
    return max_unique_word
    pass
