def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1] if len(txt) > 0 else None
    
    # Check if the last character is a letter
    is_letter = last_char.isalpha() if last_char else True
    
    # Check if the last character is not part of a word
    is_not_part_of_word = last_char != '-' and last_char != '_' and last_char != ' '
    
    # Return the boolean result
    return is_letter and is_not_part_of_word