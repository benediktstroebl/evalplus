
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return None
    # if words is not empty

    max_str = words[0]
    max_len = len(set(max_str))
    for word in words:
        # using set() to calculate the unique chars
        if len(set(word)) > max_len:
            max_len = len(set(word))
            max_str = word

    return max_str
