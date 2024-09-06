
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Can be done with a dictionary, but we'll go for a set.

    # Our set contains the set of characters for each word.
    # Note that this is a set of sets.
    chars = {}

    # For each word, create a set of characters and store in dictionary
    for word in words:
        chars[word] = set(word)

    # Track max_chars and max_chars_word
    max_chars = -1
    max_chars_word = ""

    # For each word in chars, if number of unique chars is > than the
    # current max, update max chars and the corresponding word
    for word in chars:
        if len(chars[word]) > max_chars:
            max_chars = len(chars[word])
            max_chars_word = word

    return max_chars_word



