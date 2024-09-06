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

    # Check if the last character is an alphabetical character
    if not last_char.isalpha(): 
        return False

    # Check if the last character is part of a word
    if last_char != txt.split(' ')[-1][-1]: 
        return False
    return True