
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    most = 0
    for item in words:
        if len(set(item)) > most:
            most = len(set(item))
            max_string = item
        elif len(set(item)) == most:
            if item < max_string:
                max_string = item

    return max_string


