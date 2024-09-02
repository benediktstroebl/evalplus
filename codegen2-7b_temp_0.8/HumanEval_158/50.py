
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max = ""
    max_words = {}
    for word in words:
        if word not in max_words:
            max_words[word] = word
        else:
            max_words[word] = ""
    for word in max_words:
        if max_words[word] == "":
            max = word
            break
    return max

