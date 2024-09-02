
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_words = {}
    max_len = 0
    max_word = ""
    for word in words:
        word = word.strip()
        len_word = len(set(word))
        if len_word > max_len:
            max_len = len_word
            max_word = word
        elif len_word == max_len:
            if word < max_word:
                max_word = word
    return max_word

