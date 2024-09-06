
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = max(len(word) for word in words)
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if max_chars == len(unique_chars):
            max_word = word
        elif max_chars < len(unique_chars):
            max_word = word
        else:
            max_word = word[:-1]
    return max_word
