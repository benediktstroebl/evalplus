
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char = ""
    max_len = 0
    for word in words:
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        char_count = dict(sorted(char_count.items(), key=operator.itemgetter(1),reverse=True))
        if char_count.__len__() > max_len:
            max_len = char_count.__len__()
            max_char = word
    return max_
