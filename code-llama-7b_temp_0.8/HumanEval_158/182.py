
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_word = ""
    unique_characters = set()

    for word in words:
        # check the uniqueness of characters in the current word
        # if a character is not in the set, add it.
        # if it is already in the set, do nothing.
        # else, set is updated with the new character
        for character in word:
            unique_characters.add(character)

        # update max_word if the new word has the maximum length
        if len(unique_characters) > len(max_word):
            max_word = word

        # reset the set as the current word will not be the max_word anymore
        unique_characters = set()

    return max_word
