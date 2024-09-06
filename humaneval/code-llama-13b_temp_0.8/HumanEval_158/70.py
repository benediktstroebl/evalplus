
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

    words = list(map(lambda word: (word, len(set(word))), words))

    if len(words) == 1:
        return words[0][0]

    words.sort(key=lambda item: item[1])

    max_ = words[-1][1]
    words = list(filter(lambda item: item[1] == max_, words))

    words.sort(key=lambda item: item[0])
    return words[0][0]

