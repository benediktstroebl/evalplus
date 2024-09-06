def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.

    Examples:
    >>> check_if_last_char_is_a_letter("apple pie")
    False
    >>> check_if_last_char_is_a_letter("apple pi e")
    True
    >>> check_if_last_char_is_a_letter("apple pi e ")
    False
    >>> check_if_last_char_is_a_letter("")
    False
    """
    # Ensure the input is a string and is not empty
    if not isinstance(txt, str) or not txt:
        return False
    
    # Extract the last character and check if it is alphabetical
    last_char = txt[-1]
    if not isinstance(last_char, str) or last_char.isalpha() == False:
        return False
    
    # Split the input string into words and check if the last character is an end-of-word character
    words = txt.split()