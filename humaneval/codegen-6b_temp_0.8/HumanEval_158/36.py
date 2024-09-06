
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words: return ""
    if len(words) == 1: return words[0]
    max_string = ""
    max_char = ""
    for word in words:
        if word not in max_string:
            if word in max_char:
                max_string, max_char = max_char, word
            else:
                max_string, max_char = word, word
    return max_char
