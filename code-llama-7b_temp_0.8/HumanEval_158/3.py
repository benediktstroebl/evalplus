
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
    word_len = len(words[0])
    word_count = 0
    for word in words:
        if word_len < len(word):
            word_len = len(word)
            word_count = 0
        word_count += len(set(word))
        if word_count > len(set(words[0])):
            return word
    return words[0]

