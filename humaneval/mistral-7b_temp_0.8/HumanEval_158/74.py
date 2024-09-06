
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    import string
    import collections
    first = 0
    second = ""
    for word in words:
        if first == 0:
            first = word
            second = word
        else:
            count = 0
            for i in range(0,len(first)):
                if first[i] == word[i]:
                    pass
                else:
                    count += 1
            if count == len(first):
                second = word
                first = word
    return first
