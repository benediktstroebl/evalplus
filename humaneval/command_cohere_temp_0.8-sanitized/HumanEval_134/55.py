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
    
    # Use slicing to extract the last character and transform it to lowercase
    last_char = txt[-1].lower()
    
    # Check if the last character is in lowercase
    if not last_char.isalpha():
        return False
    
    # Check if the last character is part of a word
    words = txt.split()
    if last_char in words[-1]:
        return False
    
    return True