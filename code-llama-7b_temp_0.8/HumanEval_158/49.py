
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = [list(word) for word in words]
    if len(words) == 1:
        return words[0]

    while len(words) > 1:
        words = [list(word) for word in words if list(word) not in words[:words.index(word)]]

    return ''.join(words[0])

