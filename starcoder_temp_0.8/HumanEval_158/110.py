
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_str = ""
    max_unique_char = 0
    for word in words:
        word_unique_char = len(set(word))
        if word_unique_char > max_unique_char:
            max_unique_char = word_unique_char
            max_str = word
        elif word_unique_char == max_unique_char:
            if word < max_str:
                max_str = word
    return max_str
