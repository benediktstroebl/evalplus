
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_string = words[0]
    max_unique_char = len(set(max_string))
    for word in words:
        word_unique_char = len(set(word))
        if word_unique_char > max_unique_char:
            max_string = word
            max_unique_char = word_unique_char
        elif word_unique_char == max_unique_char:
            if word < max_string:
                max_string = word
                max_unique_char = word_unique_char
    return max_string

