
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Initialize a dictionary for each string in words to store the count of each character
    char_count = {}

    # Iterate over each string in words
    for word in words:
        # Initialize a set to store the unique characters in the current string
        unique_chars = set()

        # Iterate over each character in the current string
        for char in word:
            # If the character is not in the set, add it to the set and update the char_count dictionary
            if char not in unique_chars:
                unique_chars.add(char)
                char_count[char] = char_count.get(char, 0) + 1

    # Find the string with the maximum number of unique characters
    max_string = None
    max_count = 0
    for word, count in char_count.items():
        # If the count is greater than or equal to the maximum count, update the maximum count and the string
        if count >= max_count:
            max_string = word
            max_count = count

    # If there is a tie between strings with the maximum
