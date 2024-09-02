
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # YOUR CODE HERE

    max = ""
    list_uniq = []
    for word in words:
        unique = sorted(set(word))
        if len(unique) > len(list_uniq):
            list_uniq = unique
            max = word
        elif len(unique) == len(list_uniq):
            if word < max:
                max = word
    return max



