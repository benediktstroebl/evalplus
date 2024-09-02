
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_len = 0
    max_unique = ''
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            max_unique = word
    unique_chars = set()
    for letter in max_unique:
        unique_chars.add(letter)
    if len(unique_chars) == max_len:
        return max_unique
    else:
        return None
