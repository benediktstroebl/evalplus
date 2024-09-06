
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_with_max_chars = ""
    max_chars = 0
    for word in words:
        if len(word) > max_chars:
            max_chars = len(word)
            word_with_max_chars = word
        elif len(word) == max_chars:
            if word < word_with_max_chars:
                word_with_max_chars = word

    return word_with_max_chars

