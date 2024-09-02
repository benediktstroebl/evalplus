
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = sorted(words, key=lambda s: s, reverse=True)
    max_char = ""
    max_count = 0
    for word in words:
        word_count = count_unique_character(word)
        if word_count > max_count:
            max_count = word_count
            max_char = word
    return max_char

