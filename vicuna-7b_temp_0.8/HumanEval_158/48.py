
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # initialize an empty set to store the unique characters
    unique_chars = set()
    # iterate over the list of words
    for word in words:
        # for each character in the word
        for char in word:
            # if the character is not in the set of unique characters
            if char not in unique_chars:
                # add the character to the set of unique characters
                unique_chars.add(char)
        # check if the set of unique characters is empty
        if unique_chars == set():
            return "".join(words)
    # if we have reached this point, it means
    # that there are multiple words with maximum number
    # of unique characters and we need to sort them
    # lexicographically and return the first one
    return words[0]
