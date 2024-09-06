
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Initialize a dictionary that stores word as key and the number of unique characters as value
    word_count = {}

    # Iterate over the words list
    for word in words:
        # Initialize a set to store unique characters in a word
        unique_chars = set(word)
        # Store the number of unique characters in the dictionary
        word_count[word] = len(unique_chars)

    # Sort the dictionary based on values
    sorted_dict = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Return the word with maximum number of unique characters
    return sorted_dict[0][0]
