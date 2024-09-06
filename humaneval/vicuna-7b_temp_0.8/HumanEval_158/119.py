
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = set()
    max_len = 0
    max_word = ""
    for word in words:
        char_count = len(word)
        if char_count > max_len:
            max_len = char_count
            max_word = word
    for c in max_word:
        if c not in unique_chars:
            unique_chars.add(c)
            max_len -= 1
    return max_word
