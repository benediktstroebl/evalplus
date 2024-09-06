def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to retrieve the last character
    len_txt = len(txt)
    
    # Check if the string is empty
    if len_txt == 0:
        return False
    
    # Check if the last character is a letter and it is not the last character of a word
    return txt[-1].isalpha() and not txt.split()[-1].isalpha()