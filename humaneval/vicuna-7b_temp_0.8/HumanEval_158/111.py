
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_chars = 0
    for word in words:
        # convert word to lowercase and remove whitespace
        word = word.lower().strip()
        # count unique characters in the word
        char_count = len(set(word))
        # update max_chars and max_word if necessary
        if char_count > max_chars:
            max_chars = char_count
            max_word = word
        elif char_count == max_chars and word > max_word:
            max_chars = char_count
            max_word = word
    return max_word
