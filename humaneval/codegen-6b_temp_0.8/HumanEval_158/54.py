
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
    max_str_count = 0
    for word in words:
        cur_str_count = len(set(word))
        if cur_str_count > max_str_count:
            max_str = word
            max_str_count = cur_str_count
    return max_str
