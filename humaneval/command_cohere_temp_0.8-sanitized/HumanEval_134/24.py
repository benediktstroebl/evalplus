def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any trailing spaces
    if txt and isinstance(txt, str):
        txt = txt.rstrip(' ')
    
    # Check if the string ends with a letter that is not part of a word
    if txt and txt[-1].isalpha() and not txt[-1].isalpha(True):
        return True
    return False