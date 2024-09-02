
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_unique = 0
    max_unique_word = ""
    for word in words:
        unique = set(word)
        if len(unique) > max_unique:
            max_unique = len(unique)
            max_unique_word = word
        elif len(unique) == max_unique:
            if word < max_unique_word:
                max_unique_word = word

    return max_unique_word
