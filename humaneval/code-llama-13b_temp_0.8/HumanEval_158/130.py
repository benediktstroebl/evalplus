
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
        return
    
    max_chars = 0
    unique_chars = 0
    word = ""
    # we assume the first word has the most unique characters
    for w in words:
        unique_chars = len(set(w))
        if unique_chars > max_chars:
            max_chars = unique_chars
            word = w
    
    return word
    
