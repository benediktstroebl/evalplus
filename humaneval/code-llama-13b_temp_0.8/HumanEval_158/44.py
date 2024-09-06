
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

    word = words[0]
    max_word = word

    for w in words[1:]:
        if len(w) > len(max_word):
            max_word = w
        elif len(w) == len(max_word):
            if w < max_word:
                max_word = w

    return max_word



