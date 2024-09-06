
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # create a set of all characters in all strings
    char_set = set(word.count("0123456789") for word in words)

    # find the word with maximum number of unique characters
    max_words = []
    max_chars = 0
    for word in words:
        word_chars = set(word.count("0123456789"))
        if max_chars < len(word_chars):
            max_words = [word]
            max_chars = len(word_chars)

    if max_words:
        return max_words[0]
    else:
        return "".join(sorted(words, key=lambda x: len(x)))
