
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = sorted(words)
    word_dict = {}
    for i in words:
        word_dict[i] = len(set(i))
    max_value = max(word_dict.values())
    for key, value in word_dict.items():
        if value == max_value:
            return key
    return 0

