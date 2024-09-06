
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # TODO: complete this function
    # make sure to return the first occurrence of the word
    #
    # if more than one word has the same number of unique characters,
    # return the one that comes first in lexicographical order.
    #
    # **Important**: you'll need to use the `set()` function
    #
    # [https://www.w3schools.com/python/ref_func_set.asp]
    #

    max_count = 0
    max_word = ''

    for word in words:
        count = len(set(word))
        if count > max_count:
            max_word = word
            max_count = count

    return max_word


