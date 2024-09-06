def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty and has a last character
    if not txt or not txt[-1]:
        return False
    
    # Check if the last character is a letter
    if txt[-1].isalpha():
        # Check if the last character is part of a word
        if not txt.rsplit(' ', 1)[-1].startswith(txt[-1]):
            return True
    return False