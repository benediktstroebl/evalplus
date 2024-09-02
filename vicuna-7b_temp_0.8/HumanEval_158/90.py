
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_words = []
    max_len = 0
    max_char = ""
    for word in words:
        count = 0
        for c in word:
            count += 1
        if count > max_len:
            max_len = count
            max_word = word
            max_char = max_char + c
    return max_word
