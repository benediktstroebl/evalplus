
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
        return ""
    
    max_chars = 0
    max_word = ""
    for word in words:
        cur_word = list(set(word))
        if len(cur_word) > max_chars:
            max_word = word
            max_chars = len(cur_word)
    return max_word
        

