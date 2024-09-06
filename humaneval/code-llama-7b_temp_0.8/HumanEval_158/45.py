
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = None
    max_unique = -1
    for word in words:
        unique = 0
        chars = set()
        for char in word:
            if char not in chars:
                chars.add(char)
                unique += 1
        if unique > max_unique:
            max_word = word
            max_unique = unique
    return max_word
