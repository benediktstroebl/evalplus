
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = 0
    max_name = ""
    for i in range(len(words)):
        max_len = len(set(words[i]))
        if max_len > max_len:
            max_name = words[i]
            max_len = len(set(words[i]))
    if max_len == 0:
        return ""
    else:
        return max_name
