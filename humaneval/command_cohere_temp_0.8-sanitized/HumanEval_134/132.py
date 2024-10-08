def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Define the last character variable
    last_char = txt[str_len]
    # Check if the string length is smaller than one and return False if so
    if str_len < 1:
        return False
    # Check if the last character is a letter and it is not preceded by a space
    elif last_char.isalpha() and txt[str_len - 1] != ' ':
        return True
    # If the conditions are not met, return False
    else:
        return False