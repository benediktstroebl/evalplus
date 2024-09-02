
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return None

    max_word = ""
    max_chars = 0

    for word in words:
        word_len = len(word)
        left = word_len

        while left > 0 and word[left - 1] == word[max_chars]:
            left -= 1

        if left == 0 or max_chars < left:
            max_chars = left
            max_word = word

    return max_word

