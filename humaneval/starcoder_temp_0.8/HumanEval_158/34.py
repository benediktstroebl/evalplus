
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def find_max_word(words, max_num, max_word):
        if not words:
            return max_word
        elif len(words[0]) > max_num:
            return find_max_word(words[1:], len(words[0]), words[0])
        else:
            return find_max_word(words[1:], max_num, max_word)

    return find_max_word(words, 0, "")
