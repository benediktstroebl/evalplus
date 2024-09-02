
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # your code goes here
    sorted_words = sorted(words, key=len)
    max_len = max([len(s) for s in sorted_words])
    result = []
    for word in sorted_words:
        if len(word) == max_len:
            result.append(word)
    return result[0]
