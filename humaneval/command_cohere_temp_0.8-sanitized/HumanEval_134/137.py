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
    
    # Remove trailing spaces
    while txt and txt.endswith(" "):
        txt = txt.strip()
    
    # Check if the last character is alphabetical and not part of a word
    return txt and (txt[-1].lower() in alphabet and not word_end(txt))
def word_end(txt):
    """
    Function to check if the last character of a string is a part of a word (not a boundary character).

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."
    
    # Convert string to lowercase for case-insensitive checking
    txt = txt.lower()
    
    # Check if the last character is a letter or number and is not special character
    return txt[-1] in alphabet_numbers and txt[-2:] not in SPECIAL_CHARACTERS
SPECIAL_CHARACTERS = ["-", "_", " ", ".", "!", "?", ":", ";", "'", "\"", "<", ">", "&", ")", "}", "/", "~", "="]
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_numbers = alphabet + "0123456789"