
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Check word with maximum number of unique characters
    # Return the word which comes first in lexicographical order
    # If multiple strings have maximum number of unique characters, return
    # the one which comes first in lexicographical order
    unique = []
    for word in words:
        if len(set(word)) == len(word):
            unique.append(word)
        else:
            continue
    if len(unique) == 0:
        return None
    else:
        return min(unique)
