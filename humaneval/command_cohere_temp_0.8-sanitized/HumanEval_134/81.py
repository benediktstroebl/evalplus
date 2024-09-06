def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to retrieve the last character
    last_char = txt[-1]
    # Check if the last character is a letter and it is not an abbreviation or a suffix
    if ('a' <= last_char <= 'z') or ('A' <= last_char <= 'Z') :
        return not txt.split(' ')[-1]
    return False