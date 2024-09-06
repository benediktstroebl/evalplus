
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # A dictionary containing key value pairs
    # where key is the unique character and value is the word
    # for which this unique character appears
    word_dict = {}
    # For each word in the given list
    for word in words:
        # create a string of unique characters for this word
        unique_chars = ""
        # For each character in the word
        for char in word:
            # If the character is not present in the unique characters
            # string
            if char not in unique_chars:
                # Add the character to the unique characters string
                unique_chars += char
                # If the dictionary already contains the key
                if word_dict.has_key(unique_chars):
                    # If the value for the key is not equal to the current word
                    if word_dict[unique_chars] != word:
                        # Delete the key from the dictionary
                        del word_dict[unique_chars]
                # Else the dictionary doesn't contain the key
                else:
                    # Add the word to the dictionary
                    word_dict[unique_chars] = word
    # Get the key with maximum length
    max_key = max(word_dict.keys(), key=len)
    # Return the corresponding word
    return word_dict[max_key]





