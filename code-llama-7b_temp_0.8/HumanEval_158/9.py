
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
        if len(set(word)) not in d:
            d[len(set(word))] = word
        elif len(set(word)) == d[len(set(word))]:
            if word < d[len(set(word))]:
                d[len(set(word))] = word
    return d[max(d.keys())]
