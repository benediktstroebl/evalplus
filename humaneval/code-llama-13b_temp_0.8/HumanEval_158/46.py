
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char = 0
    result = ""
    for word in words:
        word_set = set(word)
        word_len = len(word_set)
        if word_len > max_char:
            max_char = word_len
            result = word
        elif word_len == max_char:
            if word < result:
                result = word

    return result

