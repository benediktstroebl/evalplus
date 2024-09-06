
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dic = {}
    for w in words:
        for c in w:
            dic[c] = dic.get(c, 0) + 1
    print(dic)
    print(max(dic, key=dic.get))
    return max(dic, key=dic.get
