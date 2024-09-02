
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
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    for word in words_dict:
        if words_dict[word] == max(words_dict.values()):
            return word

    return ""

