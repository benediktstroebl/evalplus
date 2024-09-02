
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
    for word in words:
        if len(words_dict) == 0:
            words_dict[word] = len(set(word))
        else:
            words_dict[word] = len(set(word))
    max_val = max(words_dict.values())
    for key, val in words_dict.items():
        if val == max_val:
            return key
    return ''
