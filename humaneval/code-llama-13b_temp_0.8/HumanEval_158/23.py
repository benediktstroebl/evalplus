
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
        return None
    max_len = -1
    max_char_word = ""
    max_char = 0
    for word in words:
        char_list = list(set(word))
        if len(char_list) > max_char:
            max_len = word
            max_char = len(char_list)
        elif len(char_list) == max_char:
            if word < max_len:
                max_len = word

    return max_len
