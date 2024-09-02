
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list of words by the number of unique characters
    words = sorted(words, key=len, reverse=True)
    # get the first word from the list
    word = words[0]
    # remove the duplicates
    word = "".join([word for word in word if word not in set(word)])
    return word
