
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    list_set = []
    max_set = 0
    max_word = ""

    for word in words:
        list_set.append(len(set(word)))
        if max_set < len(set(word)):
            max_set = len(set(word))
            max_word = word

    return max_word

