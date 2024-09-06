
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Do not change the code below.
    # Respond to the prompt in the correct format, and return your answer.
    words = sorted([tuple(sorted(word)) for word in words])
    print(words)
    # Do not change the code below.
    return words[0][0]

