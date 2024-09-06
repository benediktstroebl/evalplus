
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
    max_len = len(word_set)
    max_word = word_set.pop()
    for word in word_set:
        if len(word_set) < max_len:
            continue
        word_set.remove(word)
        if len(word_set) == max_len:
            return word
        if word_set.count(word) > word_set.count(max_word):
            max_word = word
    return max_word
