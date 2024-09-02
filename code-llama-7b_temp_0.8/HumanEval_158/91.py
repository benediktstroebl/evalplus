
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

    word_max_count = len(words[0])
    word_max = words[0]
    for i in range(1, len(words)):
        if len(words[i]) > word_max_count:
            word_max = words[i]
            word_max_count = len(words[i])

    return word_max
