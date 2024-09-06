
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
        return ""
    words.sort()
    unique_words = set()
    for word in words:
        unique_words.add(word)
    max_length = 0
    max_word = ""
    for word in unique_words:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    return max_word

