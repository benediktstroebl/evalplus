
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_str = words[0]
    max_char = count_char(max_str)

    for word in words[1:]:
        word_char = count_char(word)
        if word_char > max_char:
            max_char = word_char
            max_str = word
    return max_str
