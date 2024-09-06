
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = len(words)
    max_word = ""
    for word in words:
        chunks = []
        max_char = 0
        for char in word:
            if char not in chunks:
                chunks.append(char)
                max_char = max(max_char, len(char))
        if len(chunks) > max_len:
            return word
        else:
            max_word = word
    return max_word
