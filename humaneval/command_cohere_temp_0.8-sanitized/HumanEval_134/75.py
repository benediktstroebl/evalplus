def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Check if the string is empty
    if not txt:
        return False

    # Remove trailing spaces (if any) as they shouldn't be considered as part of a word
    txt = txt.rstrip()

    # Check if the last character is a letter and not the last character of a word
    return txt[-1].isalpha() and not txt.rsplit(' ', 1)[-1].isalpha()