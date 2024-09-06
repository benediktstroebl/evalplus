
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # words = ["name", "of", "string"]
    # words = ["name", "enam", "game"]
    # words = ["aaaaaaa", "bb", "cc"]
    # words = ["ba", "ba", "ba"]
    # words = ["ba", "ba", "bac"]
    # words = ["abba", "bab", "bab"]
    # words = ["aba", "bab", "bab"]
    # words = ["aba", "bab", "bbb"]
    # words = ["abba", "bab", "bbb"]
    words = ["aba", "bab", "bbb", "baba"]


    words_dict = {}

    for word in words:
        for char in word:
            if char in words_dict:
                words_dict[char] += 1
            else:
                words_dict[char] = 1
    # for word in words:
    #     for char in word:
    #         if char not in words_dict:
    #             words_dict[
