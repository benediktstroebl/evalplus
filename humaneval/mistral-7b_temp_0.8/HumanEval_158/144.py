
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Return the word with maximum number of unique characters
    # from the list of words.
    # If multiple strings have maximum number of unique characters,
    # return the one which comes first in lexicographical order.
    word = words[0]
    for word_to_compare in words:
        if count(word) > count(word_to_compare) and word_to_compare > word:
            word = word_to_compare
    return word




