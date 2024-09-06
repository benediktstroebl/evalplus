
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_of_unique = {}
    for word in words:
        dict_of_unique[word] = len(set(word))
    sorted_words = sorted(words)
    return sorted_words[0] if dict_of_unique[sorted_words[0]] == max(dict_of_unique.values()) else sorted_words[1]

