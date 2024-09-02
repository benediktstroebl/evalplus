
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # O(n * m) time, where n = number of words, m = average length of the words
    best_word = None
    best_length = 0
    for word in words:
        if len(set(word)) > best_length:
            best_length = len(set(word))
            best_word = word
    return best_word

