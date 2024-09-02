
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # find the length of all words
    max_len = max(len(word) for word in words)
    # create a dictionary
    wd = {len(word): word for word in words}
    # find the word with max length
    result = wd[max_len]
    # if there are two words with same length, simply return the word with lower ASCII code
    if len(result) != max_len:
        return wd[max_len]
    # otherwise return the word with upper ASCII code
    else:
        return min(wd[max_len], key=lambda word: word.upper())

