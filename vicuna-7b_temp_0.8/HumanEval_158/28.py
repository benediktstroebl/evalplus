
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = []
    max_word = ""
    for word in words:
        if max_chars:
            if len(max_chars) > len(word):
                return max_word
            max_chars.append(word)
        else:
            max_chars.append(word)
            if len(max_chars) > len(word):
                return max_word
            max_word = word
    return max_word