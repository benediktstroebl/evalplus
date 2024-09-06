
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # initialize a list of unique characters for each word
    # initialize max_word
    unique_characters = []
    max_word = ""

    for word in words:
        unique_characters = []
        for character in word:
            if character not in unique_characters:
                unique_characters.append(character)

        if len(unique_characters) > len(unique_characters) > len(max_word):
            max_word = word

    return max_word
