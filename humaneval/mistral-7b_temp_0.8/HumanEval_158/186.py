
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
    for w in words:
        # 'c' 'h' 'o' 'p' 'd' 'e' 'r'
        d = {}
        for c in w:
            if c not in d:
                d[c] = 0
            d[c] += 1
        if len(d) > len(res):
            res = w
    return res
