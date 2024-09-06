
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_list = {}
    for word in words:
        dict_list[word] = set(word)

    print(dict_list)
    unique_letters = sorted(dict_list, key=lambda x: len(dict_list[x]), reverse=True)
    return unique_letters[0]

