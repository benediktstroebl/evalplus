
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # raise NotImplementedError
    len_unique = 0
    best_word = None
    for word in words:
        unique = set(word)
        if len(unique) > len_unique:
            len_unique = len(unique)
            best_word = word
    return best_word
