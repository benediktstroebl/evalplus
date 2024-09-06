
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dct = {}
    for word in words:
        word_set = set(word)
        if len(word_set) not in dct:
            dct[len(word_set)] = []
        dct[len(word_set)].append(word)
    return dct[max(dct.keys())][0]
