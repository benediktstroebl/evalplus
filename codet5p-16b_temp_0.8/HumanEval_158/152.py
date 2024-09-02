
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    words = sorted(words, key=len)
    max_len = len(words[-1])
    max_unique = []
    for word in words:
        if len(word) == max_len:
            unique = set(word)
            if len(unique) == max_len:
                max_unique.append(word)
            else:
                continue
        else:
            continue

    if len(max_unique) == 1:
        return max_unique[0]
    elif len(max_unique) == 0:
        return ""
    else:
        for word in max_unique:
            if word < max_unique[0]:
                max_unique[0] = word
        return max_unique[0]
