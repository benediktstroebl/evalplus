
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_str = ""
    max_char = 0
    for str in words:
        if len(str) > max_char:
            max_str = str
            max_char = len(str)
        elif len(str) == max_char:
            max_str = str if str < max_str else max_str

    return max_str
