def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1]

    # Check if the last character is a letter of the alphabet
    if not last_char.isalpha():
        return False

    # Split the string into words using whitespace characters as separators
    words = txt.split()

    # Check if the last character is part of any word
    if last_char in words[-1]:
        return False

    return True