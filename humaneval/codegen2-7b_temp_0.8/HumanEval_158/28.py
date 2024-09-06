
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    m = {}
    for w in words:
        unique = [char for char in w]
        unique = sorted(unique)
        if w in m:
            m[w] = sorted(list(set(m[w])|set(unique)))
        else:
            m[w] = unique

    if not m:
        return ''

    return max(m.keys(), key=len)

