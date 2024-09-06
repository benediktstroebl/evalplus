
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_string = ""
    max_char = 0

    for string in words:
        char_dict = {}
        for char in string:
            if char_dict.get(char) is None:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        if len(char_dict) > max_char:
            max_char = len(char_dict)
            max_string = string

    return max_string
