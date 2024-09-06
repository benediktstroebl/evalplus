
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return
    char_dict = {}
    for word in words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    char_dict = sorted(char_dict.items(), key=lambda x: x[1])
    char_dict = dict(char_dict)
    char_dict_list = sorted(list(char_dict.items()), key=lambda x: x[0])
    return char_dict_list[-1][0]
