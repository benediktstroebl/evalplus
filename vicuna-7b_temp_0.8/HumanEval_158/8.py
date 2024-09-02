
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
    max_word = None
    for word in words:
        if len(word) > len(max_chars[-1]):
            max_chars.append(word)
        else:
            max_chars.append(max_chars[-1])
        if len(set(word)) > len(set(max_chars[-1])):
            max_chars = [word]
            max_word = word
    return max_word
