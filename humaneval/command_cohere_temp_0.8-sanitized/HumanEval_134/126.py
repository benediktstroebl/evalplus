def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    last_char = txt.strip()[-1] if txt.strip() else None
    
    # Check if the string exists and the last character is a letter
    if last_char and last_char.isalpha():
        # Check if the last character is not part of a word
        if last_char != txt.split(' ')[-1][-1]:
            return True
    
    return False