
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def get_char_set(string):
        return set(string)

    def is_char_set_longer(string1, string2):
        return len(get_char_set(string1)) > len(get_char_set(string2))

    def is_string_lexicographically_smaller(string1, string2):
        return string1 < string2

    max_word = ""
    for word in words:
        if is_char_set_longer(word, max_word):
            max_word = word
        elif is_char_set_longer(max_word, word) and is_string_lexicographically_smaller(word, max_word):
            max_word = word

    return max_word
