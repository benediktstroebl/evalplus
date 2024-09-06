
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # a = set(words)
    # print a
    # max_value = max(a, key=len)
    # print max_value
    # for word in words:
    #     if len(word) == len(max_value):
    #         print "word:", word
    #         return word
    # return ""

    newlist = sorted(words, key=lambda x: len(x), reverse=True)
    for word in newlist:
        if len(word) == len(newlist[0]):
            print "word:", word
            return word
    return ""
