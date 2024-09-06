
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word = ''
    max_words = 0
    for item in words:
        if len(item) >= max_words:
            if len(set(item)) > max_words:
                max_words = len(set(item))
                word = item
            elif len(set(item)) == max_words and item < word:
                max_words = len(set(item))
                word = item
    return word


