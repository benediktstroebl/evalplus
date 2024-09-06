
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    d = {}
    for i in words:
        if len(i) not in d:
            d[len(i)] = [i]
        else:
            d[len(i)].append(i)
    if len(d) != 0:
        return d[max(d)][0]
    else:
        return ""
