def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1]

    # Check if the last character is a letter and not a space
    if last_char.isalpha() and (last_char != " "):
        # Check if the last character is part of a word or not
        if last_char.lower() != txt.split()[-1]:
            return True
    return False