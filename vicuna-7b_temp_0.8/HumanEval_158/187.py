
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    n = 0
    max_char = ""
    max_word = ""
    for word in words:
        unique_chars = sum([1 for char in word if char not in max_char])
        if unique_chars > n:
            n = unique_chars
            max_char = max(max_char, len(word))
        if word not in max_word:
            max_word = word
    return max_word
