
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest_word = ""
    char_count = 0
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) == len(longest_word):
            char_count = len(set(word))
            longest_word = word if char_count > len(set(longest_word)) else longest_word
        else:
            continue
    return longest_word

