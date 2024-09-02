
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list of strings
    words = sorted(words)
    max_index = 0
    max_word = ""
    for i in range(len(words)):
        # get the length of the current word
        word_len = len(words[i])
        # check if the current word is the longest
        if word_len > max_word:
            max_word = word_len
            max_index = i
    return words[max_index]
