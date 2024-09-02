
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = 0
    max_word = None
    for w in words:
        if len(set(w)) == max_len or (len(set(w)) == max_len and w < max_word):
            max_word = w
            max_len = len(set(w))
        elif len(set(w)) == max_len:
            max_word = None
    return max_word

