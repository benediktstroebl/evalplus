
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # 1st solution - sort
    # words.sort()
    # max_word = ""
    # max_count = 0
    # for word in words:
    #     if len(word) > max_count:
    #         max_word = word
    #         max_count = len(word)
    # return max_word

    # 2nd solution - dictionary
    d = {}
    for word in words:
        d[word] = len(set(word))
    return max(d, key=d.get)
    # return sorted(d.items(), key=lambda x: x[1])[-1][0]
