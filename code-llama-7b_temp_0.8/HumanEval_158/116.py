
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_unique = max_len = 0
    word_with_max_unique = ""
    for word in words:
        if len(set(word)) > max_unique:
            max_unique = len(set(word))
            word_with_max_unique = word

        if len(word) > max_len:
            max_len = len(word)

    if len(word_with_max_unique) == 0:
        return word_with_max_unique

    for word in words:
        if len(set(word)) == max_unique and word < word_with_max_unique:
            word_with_max_unique = word

    return word_with_max_unique
