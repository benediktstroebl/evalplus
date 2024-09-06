
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # if list is empty
    if len(words) == 0:
        return None

    # if list contains only one word
    if len(words) == 1:
        return words[0]

    # if list contains only two words
    if len(words) == 2:
        return words[1] if len(words[0]) < len(words[1]) else words[0]

    # sort the words in descending order
    words = sorted(words, reverse=True)

    # if there are two words with same number of unique characters
    if len(words[0]) == len(words[1]):
        return words[1] if words[0] < words[1] else words[0]

    # return the word with maximum number of unique characters
    return words[0]

