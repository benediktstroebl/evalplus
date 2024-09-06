
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # First, let's create a function that will return the number of unique characters in a string
    def get_unique_characters(word):
        unique_characters = set(word)
        return len(unique_characters)

    # Let's sort the strings by the number of unique characters in descending order
    sorted_words = sorted(words, key=get_unique_characters, reverse=True)

    # Let's return the first word in the sorted list
    return sorted_words[0]

