
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    m = None
    l = None
    for w in words:
        if l is None or len(w) > len(l):
            m = w
            l = w
        elif len(w) == len(l):
            s = sorted([w, l])
            if w < l:
                l = s[0]
            else:
                m = s[0]
    return m

