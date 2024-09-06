
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
    else:
        max_char = 0
        max_char_string = ""
        for word in words:
            word_unique_chars = len(list(set(word)))
            if word_unique_chars > max_char:
                max_char = word_unique_chars
                max_char_string = word
        return max_char_string
