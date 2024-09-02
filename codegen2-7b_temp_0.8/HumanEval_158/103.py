
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    s = []
    for w in words:
        if len(w) not in s:
            s.append(len(w))
    max_str = ""
    for w in words:
        if len(w) == s[0]:
            max_str = w
    if len(max_str) == 0:
        return ""
    else:
        return max_
