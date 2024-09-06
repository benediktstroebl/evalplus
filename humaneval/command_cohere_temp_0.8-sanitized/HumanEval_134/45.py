def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a string variable to store the last character
    last_char = txt[-1]

    # Check if the last character is a letter and return True if it is
    if last_char.isalpha():
        return True

    # Check if the last character is not part of a word and return False if it is not
    # Handle empty strings, as they have no last character
    if txt.strip():
        return last_char not in txt.rstrip('.').split()

    # Return False if the input string is empty
    return False