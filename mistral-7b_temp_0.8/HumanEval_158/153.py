
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # Initialize the maximum string with None
    max_str = None

    # Iterate over all strings
    for str in words:
        # If the string is not empty and is not max_str
        if str and str != max_str:
            # Initialize the set of unique characters in the string
            set_unique_chars = set()

            # Iterate over all characters in the string
            for char in str:
                # If the character is not already in the set of unique characters
                if char not in set_unique_chars:
                    # Add the character to the set
                    set_unique_chars.add(char)

            # If the set of unique characters is not empty and is not in the set of unique characters of max_str
            if len(set_unique_chars) > 0 and len(set(set_unique_chars)) > 0:
                # Compare the length of the set of unique characters of the string with the set of unique characters of max_str
                if len(set_unique_chars) > len(set(set(max_str))
