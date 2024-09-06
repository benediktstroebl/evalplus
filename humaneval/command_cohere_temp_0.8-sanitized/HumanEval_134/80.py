def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to be evaluated.

    Returns:
        bool: True if the last character is a letter not belonging to a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1]

    # Check if the last character is a letter and if the last character is whitespace or a newline
    if last_char.isalpha() and (last_char == ' ' or last_char == '\n'):
        # Split the string into words using whitespace as the delimiter
        words = txt.split()
        # Check if the last character is not part of a word
        if last_char not in words:
            return True
    return False