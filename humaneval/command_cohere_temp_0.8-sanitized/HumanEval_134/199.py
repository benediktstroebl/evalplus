def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words based on spaces
    words = txt.split()
    final_char = words[-1][-1] if len(words) > 0 else None
    
    return final_char is not None and final_char.isalpha() and not final_char.isalpha().isalnum()