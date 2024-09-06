
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
    if len(words) == 1:
        return words[0]
    word = words[0]
    char_count = 1
    for word in words[1:]:
        if len(word) > len(word.replace(word[0], "")):
            word = word[0] + word[1:]
        if len(word) < len(char_count * word):
            word = word[0]
            char_count = len(word)
    return
