
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    list_of_unique_chars = []
    for i in words:
        unique_chars = set(i)
        list_of_unique_chars.append(unique_chars)
    max_num_of_unique_chars = max(list_of_unique_chars, key=len)
    for i in words:
        if max_num_of_unique_chars == set(i):
            return i

