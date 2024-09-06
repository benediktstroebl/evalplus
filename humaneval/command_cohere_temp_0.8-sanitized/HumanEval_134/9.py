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

    # If the string is empty, return False
    if not txt:
        return False

    # Extract the last character and convert to lower case
    last_char = txt.strip()[-1].lower()

    # Split the string into words using space as delimiter
    words = txt.split()
    
    # Check if the last character is not part of a word
    # and it is an alphabetical character
    return last_char not in words and last_char.isalpha()