
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    for word in words:
        # start a new word
        if word:
            # compare the word with the current word to be saved
            if len(word) > len(word_to_save):
                word_to_save = word
            # if equal, compare lexicographically
            if len(word) == len(word_to_save):
                word_to_save = min(word, word_to_save)
    return word_to_save
