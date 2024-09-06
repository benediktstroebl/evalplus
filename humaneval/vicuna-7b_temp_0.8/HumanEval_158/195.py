
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = max([len(word) for word in words])
    max_word = ""
    for word in words:
        word_set = set(word)
        if len(word_set) == max_len:
            max_word = word
        if word_set < word_set[0]:
            break
    return max_word
