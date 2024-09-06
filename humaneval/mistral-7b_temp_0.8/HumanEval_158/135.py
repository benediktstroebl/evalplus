
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # You can use a helper function to calculate the number of unique characters
    # in a string
    # unique_characters_count("name") == 4
    # unique_characters_count("enam") == 4
    # unique_characters_count("aaaaaaa") == 1
    # unique_characters_count("bb") == 2
    # unique_characters_count("cc") == 2

    # Then, compare the number of unique characters using the helper function
    # with the other strings to find the one with the highest number of unique
    # characters

    # If multiple strings have the maximum number of unique characters, then
    # compare them lexicographically to find the one that comes first.

    # If there are still multiple strings with the same number of unique
    # characters and the same lexicographical order, then return the first one in
    # the list.

    # Finally, return the word with the maximum number of unique characters.

    # Your solution will be tested with different inputs.
    # Be sure to handle edge cases such as empty lists or lists with a
