
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_dict = {}
    max_word = ""
    max_length = 0
    for word in words:
        word_set = set(word)
        length = len(word_set)
        if length not in word_dict:
            word_dict[length] = [word]
        else:
            word_dict[length].append(word)
    for key, val in word_dict.items():
        if max_length < key:
            max_length = key
            max_word = val[0]
        elif max_length == key and len(max_word) > len(val[0]):
            max_word = val[0]
        elif max_length == key and len(max_word) == len(val[0]):
            if max_word > val[0]:
                max_word = val[0]
    return max_word

