
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return None
    word_length = 0
    unique_chars = 0
    result = ""
    for word in words:
        if len(word) > word_length:
            word_length = len(word)
            unique_chars = len(set(word))
            result = word
        elif len(word) == word_length:
            if len(set(word)) > unique_chars:
                unique_chars = len(set(word))
                result = word
    return result
