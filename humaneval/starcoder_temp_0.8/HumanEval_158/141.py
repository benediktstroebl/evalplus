
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_word = ""
    max_char_count = 0

    for word in words:
        char_set = set()
        for char in word:
            char_set.add(char)
        if len(char_set) > max_char_count:
            max_char_count = len(char_set)
            max_word = word
    return max_word
