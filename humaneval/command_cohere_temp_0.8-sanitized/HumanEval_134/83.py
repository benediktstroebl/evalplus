def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and assign the variable for the last character in the input string
    last_char = txt[-1] if len(txt) > 0 else None
    
    # Check if the last character is alphabetical
    is_alphabetical = last_char is not None and last_char.isalpha()
    
    # Check if the last character is not part of a word
    is_not_part_of_word = True if is_alphabetical and txt.rsplit(' ', 1)[-1] == last_char else False
    
    # Return the boolean result of the condition:
    return is_alphabetical and is_not_part_of_word