
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
    for word in words:
        if len(word) in d:
            d[len(word)] += [word]
        else:
            d[len(word)] = [word]
    max_len = max(d.keys())
    if len(d[max_len]) == 1:
        return d[max_len][0]
    else:
        return sorted(d[max_len])[0]
