
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # Find the longest word
    longest = max(words, key=len)

    # Create a set of unique letters
    unique = set(longest)

    for word in words:
        # If the word is the longest and has the same unique letters
        if word == longest and set(word) == unique:
            return word

        # If the word is not the longest but has the same unique letters
        elif set(word) == unique:
            return word

    # If the word is not the longest but has the same unique letters
    return longest

