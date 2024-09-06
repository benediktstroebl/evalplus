
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Create a list that contains a list of unique chars of each word in the
    # given list.
    unique_chars = [list(set(word)) for word in words]
    # Find out the word with maximum number of unique characters
    most_unique = words[unique_chars.index(max(unique_chars))]
    return most_unique
