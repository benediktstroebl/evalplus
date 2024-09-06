def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: Indicating whether the last character is an alphabetical character and not part of a word.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."
    
    # Check if the string is empty
    if not txt:
        return False
    
    # Split the string into words
    words = txt.split()
    
    # Check if the string ends with a space
    if words[-1] == ' ':
        return False
    
    # Get the last character
    last_char = words[-1][-1]
    
    # Check if the last character is alphabetical
    if not isinstance(last_char, str):
        return False
    if not str(last_char).isalpha():
        return False
    
    # Check if the last character is part of a word
    if last_char in words:
        return False
    
    return True