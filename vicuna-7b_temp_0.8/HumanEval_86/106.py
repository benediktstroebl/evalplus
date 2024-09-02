
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Use a set to store unique characters in the string
    unique_chars = set()
    # Loop through the string and find the length of the longest sub-string
    # of repeating characters
    max_length = 1
    for char in s:
        if char in unique_chars:
            length = len(str(unique_chars.count(char)))
            if length > max_length:
                max_length = length
    # Create a new string with the characters arranged in ascending order
    return ''.join([chr(ord(char) + max_length - 1) for char in s])
