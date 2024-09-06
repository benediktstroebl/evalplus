
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # traverse list of words
    for word in words:
        # create set of characters
        chars = set(word)
        # sort characters alphabetically
        sorted_chars = sorted(chars)
        # make a string of characters
        sorted_chars = ''.join(sorted_chars)
        # check if current word has higher number of unique characters
        if len(chars) > len(set(sorted_chars)):
            # if yes return the word
            return word
    # if all words have the same number of unique characters return the first one in list
    return words[0]
