
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return []
    if len(words) == 1:
        return words[0]

    if len(words) == 2:
        a, b = words[0], words[1]
        if len(a) > len(b):
            return a
        else:
            return b

    if len(words) > 2:
        a, b, c = words[0], words[1], words[2]
        if len(a) == len(b) and len(b) == len(c):
            if a > b:
                return a
            else:
                return b
        elif len(a) < len(b) and len(b) == len(c):
            return b
        elif len(a) < len(c):
            return c
        else:
            return a
