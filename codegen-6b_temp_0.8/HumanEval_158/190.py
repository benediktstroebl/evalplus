
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char_count = -1
    max_char_word = ""
    for word in words:
        # character count of this word
        word_len = len(word)
        char_count = 0
        for char in set(word):
            char_count += word.count(char)
        char_count = word_len - char_count
        if char_count > max_char_count:
            max_char_count = char_count
            max_char_word = word
    return max_char_word


assert(find_max(["name", "of", "string"]) == "string")
assert(find_max(["name", "enam", "game"]) == "enam")
assert(find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa")

