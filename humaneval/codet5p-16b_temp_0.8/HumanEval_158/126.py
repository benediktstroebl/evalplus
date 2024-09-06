
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
        return ''
    unique_chars = {}
    for word in words:
        for ch in word:
            if ch in unique_chars:
                unique_chars[ch] += 1
            else:
                unique_chars[ch] = 1
    max_chars = 0
    max_word = ''
    for word in words:
        if len(word) == max_chars:
            max_word = min(word, max_word)
        elif len(word) > max_chars:
            max_word = word
            max_chars = len(word)
    return max_word

