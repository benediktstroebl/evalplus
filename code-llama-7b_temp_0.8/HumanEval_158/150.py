
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    maximum_unique_characters = 0
    result = ""

    for word in words:
        characters = {}
        for char in word:
            characters[char] = 1

        if len(characters) > maximum_unique_characters:
            maximum_unique_characters = len(characters)
            result = word
        elif len(characters) == maximum_unique_characters:
            if word < result:
                result = word

    return result

