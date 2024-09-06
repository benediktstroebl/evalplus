
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the words by number of unique characters
    words_sorted = sorted(words, key=len, reverse=True)

    # check if there is only one word
    if len(words_sorted) == 1:
        return words_sorted[0]

    # check if there are multiple words with maximum number of unique characters
    for word in words_sorted:
        if len(word) == len(words_sorted[0]):
            # if words are of same length, compare them lexicographically
            return word if word < words_sorted[0] else words_sorted[0]

    # if multiple words have same number of unique characters, return the first one
    return words_sorted[0]
