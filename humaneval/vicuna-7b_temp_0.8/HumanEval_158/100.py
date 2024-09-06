
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the words lexicographically
    words.sort()

    # keep track of the maximum number of unique characters
    max_chars = 0
    max_word = None
    for word in words:
        chardet = chardet_url(word)
        # update the maximum number of unique characters and word if needed
        if chardet > max_chars:
            max_chars = chardet
            max_word = word
    return max_word