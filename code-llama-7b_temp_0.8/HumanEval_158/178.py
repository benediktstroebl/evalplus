
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_len = {w: len(set(w)) for w in words}
    print(words_len)
    max_len = max(words_len.values())
    word_with_max_len = [k for k, v in words_len.items() if v == max_len]
    print(word_with_max_len)
    return min(word_with_max_len)

