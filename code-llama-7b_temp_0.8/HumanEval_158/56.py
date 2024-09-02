
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
        return None
    max_length = 0
    max_item = None
    for i in range(len(words)):
        unique = len(set(words[i]))
        if unique > max_length:
            max_length = unique
            max_item = words[i]
        elif unique == max_length:
            if words[i] < max_item:
                max_item = words[i]
    return max_item
