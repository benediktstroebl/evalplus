
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
    max_len = 0
    max_word = ""
    for word in words:
        n_chars = len(word)
        if n_chars > max_len:
            max_len = n_chars
            max_word = word
    if max_word == "":
        return words[0]
    return max_word
