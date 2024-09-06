
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # list of unique chars
    unique_chars = set()

    # get unique chars from each string
    for word in words:
        unique_chars |= set(word)

    # find max
    max_word = None
    for word in words:
        num_unique_chars = len(unique_chars)
        if num_unique_chars == len(set(word)):
            # num unique chars == len(set(word))
            if not max_word:
                max_word = word
            else:
                if word < max_word:
                    max_word = word

    return max_word

