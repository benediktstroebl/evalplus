
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = len(words[0])
    for word in words:
        unique_chars = set(word)
        if max_len < len(unique_chars):
            max_len = len(unique_chars)
        if max_len == len(words[0]):
            max_len += 1
        if unique_chars == set(words[0]) and len(words[0]) == max_len:
            max_word = words[0]
        else:
            max_word = word
        words = [max_word]
    return ''.join(words)
