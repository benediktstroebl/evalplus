
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

    words = sorted(words, key=len)
    max_characters = 0
    result = ""

    for word in words:
        unique_chars = set(word)
        if len(unique_chars) >= max_characters:
            max_characters = len(unique_chars)
            result = word

    return result

