def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string"
    
    # Use the slice notation to extract the last character of the string
    last_char = txt[-1:]
    
    # Check if the last character exists and is an alphabetical character
    if last_char.isalpha() and last_char not in WORDS:
        return True
    
    return False
WORDS = ["apple", "pi", "pie", "e"]