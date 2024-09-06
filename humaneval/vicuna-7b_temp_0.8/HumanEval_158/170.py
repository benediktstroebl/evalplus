
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
    max_word = None
    for word in words:
        for char in word:
            if char.lower() not in unique_chars:
                unique_chars[char.lower()] = 1
                if max_word is None or cmp(word, max_word) > 0:
                    max_word = word
    return max_word