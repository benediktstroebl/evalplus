
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # 1. find max word len
    max_word_len = 0
    for word in words:
        if len(word) > max_word_len:
            max_word_len = len(word)

    # 2. find word with max number of unique characters
    max_word = ""
    count = 0
    for word in words:
        if len(set(word)) == max_word_len:
            count += 1
            if word < max_word:
                max_word = word

    if count > 1:
        return ""
    return max_word



























