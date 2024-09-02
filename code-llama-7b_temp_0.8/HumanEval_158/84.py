
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
        return ""

    if len(words) == 1:
        return words[0]

    max_words = []
    unique_chars = set()
    for word in words:
        if len(word) > len(unique_chars):
            unique_chars = set(word)
            max_words = [word]
        elif len(word) == len(unique_chars):
            unique_chars = set(word)
            max_words.append(word)
    if len(max_words) > 1:
        max_words.sort()
        return max_words[0]
    return max_words[0]
