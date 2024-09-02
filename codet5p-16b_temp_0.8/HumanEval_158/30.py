
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if not words:
        return ""
    
    unique_count = {}
    for word in words:
        unique_count[word] = len(set(word))

    max_unique_count = max(unique_count.values())
    return min(unique_count.keys(), key=lambda k: unique_count[k])


