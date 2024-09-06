
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_dict = {}
    for word in words:
        char_set = set(word)
        if char_set in words_dict:
            words_dict[char_set].append(word)
        else:
            words_dict[char_set] = [word]
    return sorted(words_dict[max(words_dict, key=lambda x: len(x))][0])

