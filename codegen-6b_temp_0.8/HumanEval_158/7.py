
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_map = {}
    for word in words:
        words_map[word] = len(set(word))

    words = list(words_map.items())
    words = sorted(words, key=lambda x: x[1], reverse=True)
    words_word = words[0][0]

    return words_word

