
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = 0
    result = ""
    for word in words:
        unique_word_count = len(set(word))
        if unique_word_count > max_len:
            max_len = unique_word_count
            result = word
        elif unique_word_count == max_len:
            result = min(result, word)
    return result
