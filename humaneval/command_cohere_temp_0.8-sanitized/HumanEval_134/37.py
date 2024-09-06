def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Check if the string is empty
    if not txt:
        return False

    # Remove any spaces from the end of the string and check if the last character is alphabetical
    alpha = txt.strip().lower()[-1] in alphabetical_characters
    return alpha
alphabetical_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"