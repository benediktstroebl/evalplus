
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = 0
    word = ""
    for word_i in words:
        if len(word_i) > max_chars:
            max_chars = len(word_i)
            word = word_i
        elif len(word_i) == max_chars:
            if word > word_i:
                word = word_i
    return word

