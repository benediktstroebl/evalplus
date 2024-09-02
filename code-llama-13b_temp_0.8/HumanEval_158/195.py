
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def uniq_char(word):
        return len(set(word))

    def sort_order(word_a, word_b):
        return (word_a > word_b) - (word_a < word_b)

    max_uniq_chars = 0
    res = None
    for word in words:
        word_uniq_chars = uniq_char(word)
        if word_uniq_chars > max_uniq_chars:
            max_uniq_chars = word_uniq_chars
            res = word

    return res

