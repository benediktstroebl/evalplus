
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_len = 0
    max_unique_chars = 0

    for word in words:
        word_len = len(word)
        word_unique_chars = {}

        for char in word:
            if char in word_unique_chars:
                word_unique_chars[char] += 1
            else:
                word_unique_chars[char] = 1

        unique_chars = sum(word_unique_chars.values())

        if word_len > max_len or (max_len == word_len and unique_chars > max_unique_chars):
            max_word = word
            max_len = word_len
            max_unique_chars = unique_chars

    return max_word
