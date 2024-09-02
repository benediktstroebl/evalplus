
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words.sort()

    max_ = words[0]
    for word in words:
        if len(word) > len(max_):
            max_ = word
        elif len(word) == len(max_):
            if word < max_:
                max_ = word
    return max_

