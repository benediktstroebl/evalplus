
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""
    max_unique = -1
    max_unique_word = ""
    for word in words:
        unique_char = len(set(word))
        if unique_char > max_unique:
            max_unique = unique_char
            max_unique_word = word
    return max_unique_word
