
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    l = []
    result = ""
    for e in words:
        if e not in l:
            l.append(e)
        else:
            l.remove(e)
            l.append(e)

        if len(e) > len(result):
            result = e
    return result

