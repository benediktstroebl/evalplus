
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_list = words.split()
    unique_chars = set([])
    for word in word_list:
        unique_chars |= set(word)
    max_chars = max(unique_chars)
    if len(unique_chars) == 1:
        return max_chars
    for word in word_list:
        if word[0] == max_chars:
            return word
    return ""


