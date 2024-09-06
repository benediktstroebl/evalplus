
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    result = {}
    for word in words:
        word_set = set(word)
        word_len = len(word_set)
        if word_len in result:
            if result[word_len] > word:
                result[word_len] = word
        else:
            result[word_len] = word
    return result[max(result)]
