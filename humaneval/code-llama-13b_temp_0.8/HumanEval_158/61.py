
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def char_set(s):
        return set(s)

    charsets = map(char_set, words)
    unique_characters = list(map(len, charsets))
    max_index = unique_characters.index(max(unique_characters))
    return words[max_index]


