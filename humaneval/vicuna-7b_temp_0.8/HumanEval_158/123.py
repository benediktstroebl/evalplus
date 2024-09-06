
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
    max_uniq_chars = 0
    for word in words:
        word_uniq_chars = len(set(word))
        if word_uniq_chars > max_uniq_chars:
            max_uniq_chars = word_uniq_chars
            max_word = word
    return max_word
