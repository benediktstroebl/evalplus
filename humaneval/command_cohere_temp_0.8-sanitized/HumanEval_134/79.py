import unittest
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    last_char = txt[-1:]
    if len(last_char) != 1 or not str.isalpha(last_char):
        return False
    words = txt.split()
    if last_char in words[-1]:
        return False
    return True