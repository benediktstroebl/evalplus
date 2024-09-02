
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
        return None

    def find_max_helper(words, word):
        if not words:
            return word
        new_word = word
        for w in words:
            if len(w) > len(word):
                new_word = w
        return find_max_helper(words[1:], new_word)
    return find_max_helper(words, words[0])

