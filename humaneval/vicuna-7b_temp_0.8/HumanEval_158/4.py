
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = max(len(word) for word in words)
    max_word = ""
    for word in words:
        if len(word) == max_chars:
            if word == max_word:
                return "".join(sorted(words, key=lambda x: x.lower()))
            else:
                max_word = word
    return max_word