
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_dict = {}
    max_len = 0
    max_word = ""
    for word in words:
        words_dict[word] = len(set(word))

    for key, value in words_dict.items():
        if value > max_len:
            max_len = value
            max_word = key

    return max_word
