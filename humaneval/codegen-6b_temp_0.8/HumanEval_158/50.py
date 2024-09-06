
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_index = 0
    max_char_count = 0
    for word in words:
        char_count = len(set(word))
        if char_count > max_char_count:
            max_char_count = char_count
            max_index = words.index(word)
    return words[max_index]

