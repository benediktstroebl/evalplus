
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_char = {}
    for word in words:
        unique_char[word] = len(set(word))
    sorted_unique_char = sorted(unique_char.items(), key=lambda x: (x[1], x[0]))
    return sorted_unique_char[-1][0]


