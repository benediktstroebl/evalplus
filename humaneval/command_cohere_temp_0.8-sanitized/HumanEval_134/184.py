def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # If the string is empty or there are no words at all, return False
    if not txt or not words:
        return False
    # Check if the last character is a letter and not the last character of a word
    return txt[-1].isalpha() and txt[-1] != words[-1][-1]