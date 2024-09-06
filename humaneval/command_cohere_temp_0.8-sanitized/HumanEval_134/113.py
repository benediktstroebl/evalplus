import unittest
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to avoid indexing errors
    if len(txt)==0:
        return False
    # Use slice with a step of 1 to exclude the last character
    alphabetical_chars = [c for c in txt[:-1]]
    # Check if the last character is an alphabetical character and not part of a word
    return (txt[-1].isalpha() and txt[-1] not in alphabetical_chars)