
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # use sort method to sort the words in descending order
    words = sorted(words, key=len, reverse=True)
    # use set method to get unique characters
    for word in words:
        if len(set(word)) == max(len(set(word)) for word in words):
            return word

    # if no word has maximum number of unique characters, return empty string
    return ""
