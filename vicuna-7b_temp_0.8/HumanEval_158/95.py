
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
    max_word = max(words, key=word_set.count)
    max_index = word_set.index(max_word)
    max_word = [word[0] for word in words if word[0] == max_word[0]]
    return max_word[max_index]
