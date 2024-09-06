
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
    max_word = max(words, key=word.count, key=word.lower)
    if len(set(words)) == 1:
        return max_word
    else:
        for word in words:
            if len(set(word)) == 1:
                return word
        return max_word
