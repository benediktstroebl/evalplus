
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ''

    max_string = words[0]
    max_number_of_chars = len(max_string)

    for word in words[1:]:
        if len(word) < max_number_of_chars:
            max_string = word
            max_number_of_chars = len(word)
        else:
            continue

    return max_string

