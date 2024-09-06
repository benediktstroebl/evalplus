
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # test the input
    if words is None or not isinstance(words, list):
        raise Exception("Invalid input")

    if len(words) == 0:
        raise Exception("No words")

    # sort the words by length of unique characters
    words.sort(key=lambda x: len(set(x)))
    return words[0]

