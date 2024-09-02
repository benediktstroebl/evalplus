
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # solution 1
    def sort_fn(x):
        return len(set(x))
    return min(words, key = sort_fn)

    # # solution 2
    # max_char = ""
    # max_len = 0
    #
    # for word in words:
    #     if len(word) > max_len:
    #         max_len = len(word)
    #         max_char = word
    #
    # return max_char

