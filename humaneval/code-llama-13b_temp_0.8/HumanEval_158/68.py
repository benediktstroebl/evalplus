
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return
    if len(words) == 1:
        return words[0]

    max_word = words[0]
    max_chars = {}

    for word in words:
        unique_chars = {}
        for letter in word:
            if letter not in unique_chars:
                unique_chars[letter] = 1
        if len(unique_chars) > len(max_chars):
            max_word = word
            max_chars = unique_chars
        elif len(unique_chars) == len(max_chars):
            if word < max_word:
                max_word = word
                max_chars = unique_chars

    return max_word

