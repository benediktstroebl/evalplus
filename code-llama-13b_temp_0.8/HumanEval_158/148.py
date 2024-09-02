
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return ""

    char_dict = {}
    max_chars = 0
    for i in range(len(words)):
        for char in words[i]:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        char_dict_keys = char_dict.keys()
        if len(char_dict_keys) > max_chars:
            max_chars = len(char_dict_keys)
            max_word = words[i]

        char_dict = {}

    return max_word

