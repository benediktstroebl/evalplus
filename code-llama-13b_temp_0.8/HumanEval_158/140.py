
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
        return None

    max_value = 0
    max_word = None
    for word in words:
        value = len(set(word))
        if value > max_value:
            max_value = value
            max_word = word
        elif value == max_value:
            if word < max_word:
                max_word = word

    return max_word

