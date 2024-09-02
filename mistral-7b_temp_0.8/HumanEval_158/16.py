
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    res = ""
    max_len = 0
    for word in words:
        if len(word) >= max_len:
            unique_chars = set()
            for char in word:
                if char not in unique_chars:
                    unique_chars.add(char)
            if len(unique_chars) >= max_len:
                res = word
                max_len = len(unique_chars)
    return res

