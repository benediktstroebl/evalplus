def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to check.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Extract the last character and remove any whitespace if present
    last_char = txt.strip()[-1:]
    
    # Check if the last character is a letter
    if not last_char.isalpha():
        return False
    
    # Check if the last character is not part of a word
    if last_char.isalnum(): 
        return True
    else:
        # Check if the last character is a single character and not alphabetic
        if len(last_char) == 1 and not last_char.lower() in 'xyz':
            return False
        else:
            return True