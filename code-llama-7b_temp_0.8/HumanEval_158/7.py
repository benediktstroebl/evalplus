
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return None
    # for each string in words, save the word with the maximum number of unique chars
    max_word = words[0]
    max_len = len(set(max_word))
    for word in words:
        current_len = len(set(word))
        if current_len >= max_len:
            max_word = word
            max_len = len(set(word))
    return max_word

