
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_length = 0
    max_word = ""

    for word in words:
        # Check for unique characters in each word
        unique_chars = set(word)
        # If the word has more unique characters than max_length
        if len(unique_chars) > max_length:
            # Set new max_length
            max_length = len(unique_chars)
            # Reset max_word
            max_word = word
        # If the word has same number of unique characters as max_length
        elif len(unique_chars) == max_length:
            # Check lexicographical order and update max_word
            if word < max_word:
                max_word = word

    return max_word
