def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Extract the last character and remove whitespace characters if present
    last_char = txt.strip()[-1:]
    
    # Check if the last character is a letter
    if last_char.isalpha():
        # Check if the last character is not part of a word
        if last_char != txt.strip().split(' ')[-1]:
            return True
    
    return False