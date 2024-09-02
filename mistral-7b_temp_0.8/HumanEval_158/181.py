
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # d = {}
    # for word in words:
    #     d[word] = len(set(word))
    # max_word = ""
    # for w in words:
    #     if d[w] > d[max_word] or d[w] == d[max_word] and w < max_word:
    #         max_word = w
    # return max_word

    return sorted(words, key=lambda x: (len(set(x)), x))[0]





