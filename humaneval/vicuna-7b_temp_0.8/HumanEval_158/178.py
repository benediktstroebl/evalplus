
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_set = set(words)
    max_word = max(words, key=lambda x: len(set(x)))
    max_word_idx = word_set.index(max_word)
    if max_word_idx == 0:
        return max_word
    else:
        return words[max_word_idx]
