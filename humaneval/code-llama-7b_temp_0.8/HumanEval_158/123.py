
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = {}
    max_chars = 0
    max_word = ""
    for word in words:
        unique_chars = {}
        for char in word:
            if char in unique_chars:
                unique_chars[char] += 1
            else:
                unique_chars[char] = 1
        if len(unique_chars) > max_chars:
            max_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_chars:
            if word < max_word:
                max_word = word
    return max_word
