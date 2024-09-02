
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_words = {}
    for word in words:
        word = word.lower()
        if word in max_words:
            max_words[word] += 1
        else:
            max_words[word] = 1
    max_word = max(max_words, key=max_words.get)
    return max_word