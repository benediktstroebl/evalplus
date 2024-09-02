
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    maximum_word = ""
    maximum_word_length = 0
    for word in words:
        set_word = set(word)
        if len(set_word) > maximum_word_length:
            maximum_word_length = len(set_word)
            maximum_word = word
    return maximum_word
