
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # return None
    if len(words) == 0:
        return ""
    max_words = set()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_words = {word}
            max_length = len(word)
        elif len(word) == max_length:
            max_words.add(word)
    # max_words.sort()
    # return max_words[0]
    return max(max_words)

