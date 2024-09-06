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

    # Check if the last character is lowercase or uppercase
    if last_char.isalpha(): 
        # Check if the last character is a part of a word
        if last_char == '-' or last_char == '_' or last_char == ' ' or last_char == '\n':
            return False
        else:
            return True
    else:
        return False