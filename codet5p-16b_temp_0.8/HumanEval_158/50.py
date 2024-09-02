
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    sorted_list = sorted(words, key = len)
    max_len = len(sorted_list[-1])
    max_unique = sorted_list[-1]
    for word in words:
        if len(word) == max_len:
            if len(set(word)) == max_len:
                if word < max_unique:
                    max_unique = word
    return max_unique
