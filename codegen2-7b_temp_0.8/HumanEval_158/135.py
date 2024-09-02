
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return words[0] if len(set(words[0])) > len(set(words[1])) else words[1]
    else:
        return words[0] if len(set(words[0])) > len(set(words[1])) else words[1] if len(set(words[1])) > len(set(words[2])) else words[2
