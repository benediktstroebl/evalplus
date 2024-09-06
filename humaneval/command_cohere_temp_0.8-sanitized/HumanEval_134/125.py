def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to avoid runtime errors
    if len(txt)==0:
        return False
    # Use slicing to extract the last character and convert it to lowercase for case-insensitivity
    last_char = txt[-1].lower()
    # Use a boolean OR operation to check if the last character is a letter or digit