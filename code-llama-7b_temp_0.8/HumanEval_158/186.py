
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_length = 0
    word = ""
    for i in words:
        length = len(set(i))
        if length > max_length:
            max_length = length
            word = i
        elif length == max_length:
            if i < word:
                word = i
    return word
