
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    list_of_max_unique_chars = []
    for word in words:
        list_of_max_unique_chars.append(len(set(word)))
    index_of_max_unique_chars = list_of_max_unique_chars.index(max(list_of_max_unique_chars))
    return words[index_of_max_unique_chars]

