
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique = 0
    max_unique = 0
    max_word = ""

    for word in words:
        char_count = 0
        char_set = set()
        for char in word:
            if char not in char_set:
                char_set.add(char)
                char_count += 1
        if char_count > max_unique:
            max_unique = char_count
            max_word = word
    return max_word
