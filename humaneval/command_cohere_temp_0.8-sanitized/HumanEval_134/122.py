def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string minus the last character
    incomplete_string = txt[:-1]
    # Check if the last character is part of a word
    return not txt.endswith(incomplete_string.split()) and txt[-1].isalpha()