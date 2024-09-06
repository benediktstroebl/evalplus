
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    res_word = ""
    res_chars = set()
    for word in words:
        word_chars = set(word)
        if len(word_chars) > len(res_chars):
            res_chars = word_chars
            res_word = word
        elif len(word_chars) == len(res_chars):
            if word < res_word:
                res_word = word
    return res_word



