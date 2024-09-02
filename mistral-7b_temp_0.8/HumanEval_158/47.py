
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    from collections import Counter
    s = Counter(words)
    l = []
    for key in s:
        if key != ' ':
            l.append(key)
    for word in l:
        d = Counter(word)
        #print(d)
        if len(d) > len(d1):
            d1 = d
    return d1

