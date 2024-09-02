
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    most_characters = []
    for word in words:
        if len(word) >= len(most_characters):
            most_characters = word

    for word in words:
        if len(word) > len(most_characters):
            most_characters = word

    for word in words:
        if len(word) == len(most_characters) and most_characters > word:
            most_characters = word

    return most_characters
