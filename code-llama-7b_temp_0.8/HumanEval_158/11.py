
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    res = ""
    max_len = 0
    for word in words:
        if len(set(word)) > max_len:
            max_len = len(set(word))
            res = word
        elif len(set(word)) == max_len:
            if word < res:
                res = word
    return res

