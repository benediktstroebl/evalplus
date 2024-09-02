
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_unique = 0
    max_word = ""
    for word in words:
        word_dict = {}
        for char in word:
            if char not in word_dict:
                word_dict[char] = 0
            word_dict[char] += 1
        if len(word_dict) > max_unique:
            max_unique = len(word_dict)
            max_word = word
    return max_word



