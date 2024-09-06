
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_len = 0
    max_count = 0
    for word in words:
        count = len(word)
        if count > max_len:
            max_len = count
            max_word = word
            max_count = 0
        count = len(set(word))
        if count > max_count:
            max_count = count
    return max_word