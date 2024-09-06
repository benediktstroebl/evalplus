
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = 0
    max_unique_chars = 0
    word = ""
    word_max = ""
    for word in words:
        unique_chars = 0
        for letter in word:
            if letter not in word_max:
                unique_chars += 1
        if unique_chars >= max_unique_chars:
            max_unique_chars = unique_chars
            word_max = word
    return word_max
