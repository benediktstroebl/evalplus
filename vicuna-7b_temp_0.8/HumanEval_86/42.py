
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
    # The regular expression will match any word, which is a sequence of letters
    # with no digits, and the length of the word is variable.
    pattern = r'\b\w+\b'

    # Use string.membership() method to check if the string contains only characters
    # in the range of ASCII value of a-z and A-Z.
    if not any(c.isalpha() for c in s):
        return s

    # Create a new string with the characters in ascending order based on their
    # ASCII values.
    result = ''
    for c in s:
        if c.isalpha():
            result += chr(ord(c) - ord('a') + 1)
        else:
            result += c
    return result
