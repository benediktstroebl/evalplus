
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = -1
    max_word = ""

    for word in words:
        # If the number of unique characters in the word is greater than the max
        if len(set(word)) > max_len:
            # Update max len to new max
            max_len = len(set(word))
            # And update max_word to the word itself
            max_word = word

    return max_word
