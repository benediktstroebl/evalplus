
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
        return None
    counter = {}
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(counter):
            counter = unique_chars
        elif len(unique_chars) == len(counter):
            if word < counter:
                counter = unique_chars
    return counter

