
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # store the word and its length in a dictionary
    length = {}
    for word in words:
        length[word] = len(set(word))
    # if more than one word has the maximum length of unique characters,
    # return the word that comes first in lexicographical order
    # otherwise, return an empty string
    if len(length) > 1:
        max_length = max(length.values())
        for key, value in length.items():
            if value == max_length:
                return key
    return ""
