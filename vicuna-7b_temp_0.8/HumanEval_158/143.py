
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word_len = max([len(word) for word in words])
    max_word = "".join(sorted(words, key=lambda w: len(w), reverse=True))
    max_chars = len(max_word)
    if max_chars > max_word_len:
        return "".join(sorted(words, key=lambda w: len(w), reverse=True)[0])
    else:
        return max_word
