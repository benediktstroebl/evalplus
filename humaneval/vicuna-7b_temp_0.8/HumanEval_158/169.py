
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Create a set of characters for each word
    charsets = {set(word): i for i, word in enumerate(words)}
    # Iterate through the words
    for word in words:
        # Find the length of the word
        word_length = len(word)
        # Find the number of unique characters in the word
        unique_chars = sum(word.count(c) for c in word)
        # Look up the index of the word in the character set
        word_index = charsets[set(word)]
        # If the word has more unique characters than the current max, update it
        if unique_chars > max:
            max = unique_chars
            max_word = word
    return max_word
