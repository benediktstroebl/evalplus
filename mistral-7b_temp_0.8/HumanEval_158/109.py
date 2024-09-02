
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_unique = ""
    for w in words:
        char_set = set(w)
        unique_count = len(char_set)
        if unique_count > len(max_unique):
            max_unique = w
        elif unique_count == len(max_unique) and w < max_unique:
            max_unique = w
    return max_unique

