
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_words = dict()
    max_num_unique = -1
    word_max_num_unique = ""
    for word in words:
        num_unique = len(set(word))
        if num_unique > max_num_unique:
            max_num_unique = num_unique
            word_max_num_unique = word
        elif num_unique == max_num_unique:
            if word < word_max_num_unique:
                word_max_num_unique = word
    return word_max_num_unique
