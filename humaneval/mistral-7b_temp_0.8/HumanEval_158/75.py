
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def char_count(str_):
        return len(set(str_))

    max_len_words = [word for word in words if char_count(word) == max(char_count(word) for word in words)]

    if len(max_len_words) > 1:
        return min(max_len_words)

    return max_len_words[0]
