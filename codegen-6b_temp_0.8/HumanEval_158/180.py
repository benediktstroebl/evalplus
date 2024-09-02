
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char = ""
    max_uniq_chars = 0
    word = ""
    for i in words:
        if len(i) > len(max_char):
            max_char = i
        if len(set(i)) > max_uniq_chars:
            max_uniq_chars = len(set(i))
            word = i
    return word

