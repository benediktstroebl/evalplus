
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def find_max_func(func_list):
        max_func = func_list[0]
        max_len = len(func_list[0])
        for func in func_list:
            if len(func) > max_len:
                max_func = func
                max_len = len(func)
        return max_func
    #
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    #
    return find_max_func(dict_words.keys())

