
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    char_map = {}
    max_word = ""
    for word in words:
        if word > max_word:
            max_word = word
        unique_chars = set(word)
        for c in unique_chars:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] += 1
    for word in words:
        if max_word == word:
            return max_word
        elif char_map[c] > 0:
            return max_word

