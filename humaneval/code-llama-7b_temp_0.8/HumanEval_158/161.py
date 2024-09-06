
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_unique_char = 0
    word_with_max_unique_char = None
    for word in words:
        unique_char = len(set(word))
        if unique_char > max_unique_char:
            max_unique_char = unique_char
            word_with_max_unique_char = word
        elif unique_char == max_unique_char:
            if word < word_with_max_unique_char:
                word_with_max_unique_char = word
    return word_with_max_unique_char
