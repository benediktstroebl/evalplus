
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # unique_letters = [len(set(word)) for word in words]
    # max_ = max(unique_letters)
    # for index, word in enumerate(words):
    #     if len(set(word)) == max_:
    #         return word
    return max(words, key=lambda x: (len(set(x)), x))

