
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_unique_chars = 0
    result_word = ""
    for word in words:
        unique_chars_in_word = len(set(word))
        if unique_chars_in_word > max_unique_chars:
            max_unique_chars = unique_chars_in_word
            result_word = word
    return result_word

