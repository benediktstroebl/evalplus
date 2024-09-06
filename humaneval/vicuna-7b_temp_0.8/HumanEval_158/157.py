
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    n = len(words)
    max_chars = 0
    max_word = ""
    for word in words:
        unique_chars = sum([1 for char in word if char not in set(word)])
        max_chars = max(max_chars, unique_chars)
        if max_chars > n:
            return word
        if max_chars == n and word > max_word:
            return word
        max_word = word
    return max_word
