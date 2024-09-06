
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_number_of_characters = 0
    for word in words:
        number_of_characters = set(word)
        if len(number_of_characters) > max_number_of_characters:
            max_number_of_characters = len(number_of_characters)
    result = None
    for word in words:
        number_of_characters = set(word)
        if len(number_of_characters) == max_number_of_characters:
            if result is None or word < result:
                result = word
    return result

