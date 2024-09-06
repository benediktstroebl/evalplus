
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return ""
    else:
        max_word = ""
        max_unique_chars = 0
        for word in words:
            unique_chars = len(set(word))
            if max_unique_chars < unique_chars:
                max_word = word
                max_unique_chars = unique_chars
        return max_word
