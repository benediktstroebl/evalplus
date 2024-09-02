
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_unique(word):
        return len(set(word))

    max_word = None
    max_count = 0
    for word in words:
        if count_unique(word) > max_count:
            max_word = word
            max_count = count_unique(word)

    return max_word
