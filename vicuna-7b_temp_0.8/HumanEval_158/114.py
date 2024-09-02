
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_count = {}
    for word in words:
        char_set = set(word)
        if char_set in word_count:
            word_count[char_set] += 1
        else:
            word_count[char_set] = 1
    return max(word_count, key=word_count.get)
