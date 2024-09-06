
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list by the number of unique characters
    words = sorted(words, key=lambda x: len(set(x)))

    # if the list is empty, return None
    if not words:
        return None

    # if only one word, return it
    if len(words) == 1:
        return words[0]

    # if more than one word, return the first one in lexicographic order
    # that has the maximum number of unique characters
    return words[0]
