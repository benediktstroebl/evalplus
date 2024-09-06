def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.

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
    import re

    pattern = r'\b\w*'  # Match any character that is not a space nor an alphanumeric character
    comp_pattern = re.compile(pattern) 
    compressed_txt = comp_pattern.sub('', txt)  # Compress the string to remove words
    
    return compressed_txt and compressed_txt.isalpha()