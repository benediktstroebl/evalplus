
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = {}
    # first loop to find unique chars in each word
    for word in words:
        unique_chars[word] = len(set(word))

    # second loop to find the word with max unique chars
    word_with_max_chars = ""
    for key in unique_chars:
        if unique_chars[key] > unique_chars[word_with_max_chars]:
            word_with_max_chars = key

    return word_with_max_chars

