
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # get unique characters
    unique_char_count = {}
    for word in words:
        unique_char_count[word] = len(set(word))
    
    # find the max
    max_unique_chars = max(unique_char_count.values())
    
    # return first one in order that meets the max
    for key, value in unique_char_count.items():
        if value == max_unique_chars:
            return key
