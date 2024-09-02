
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_unique = 0
    max_word = ""

    for i in words:
        unique = len(set(list(i)))
        if unique > max_unique:
            max_unique = unique
            max_word = i
        if unique == max_unique and max_word > i:
            max_word = i

    return max_word
