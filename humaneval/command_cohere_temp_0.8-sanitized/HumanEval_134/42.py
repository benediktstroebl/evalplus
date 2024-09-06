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
    
    # Use slice to remove the last character and assign to a variable
    last_char = txt[-1:]
    
    # Split the string into words using space as delimiter
    words = txt.split()
    
    # Check if the last character is not part of any word and is an alphabet character
    return last_char not in words and last_char.isalpha()