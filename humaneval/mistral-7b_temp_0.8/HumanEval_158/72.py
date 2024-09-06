
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def find_max_helper(words, current_word):
        if len(words) == 0:
            return current_word
        if len(words) == 1:
            return words[0]
        if len(words[0]) > len(current_word):
            return find_max_helper(words[1:], words[0])
        else:
            return find_max_helper(words[1:], current_word)

    return find_max_helper(words, "")
