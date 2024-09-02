
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = []
    max_length = 0
    for word in words:
        chars = set(word)
        if len(chars) > max_length:
            max_chars = chars
            max_length = len(chars)
    return ''.join(max_chars)
