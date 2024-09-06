
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list
    words = sorted(words)
    # find the length of each word
    max_len = max([len(word) for word in words])
    max_word = ""
    # iterate through the words
    for word in words:
        # find the number of unique characters
        num_chars = len(set(word))
        # check if the current word has more unique characters than the current
        # max_word and if it comes first in lexicographical order
        if num_chars > max_len:
            if word > max_word:
                max_word = word
    return max_word
