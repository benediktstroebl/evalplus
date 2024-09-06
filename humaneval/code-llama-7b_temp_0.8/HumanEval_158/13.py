
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char = 0
    res = ""
    for i in range(len(words)):
        s = list(set(words[i]))
        if len(s) > max_char:
            max_char = len(s)
            res = words[i]
        elif len(s) == max_char:
            res = min(res, words[i])
    return res

