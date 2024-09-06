
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = sorted(words)
    unique_chars = set()
    max_count = 0
    for word in words:
        unique_chars = set(word)
        count = len(unique_chars)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
