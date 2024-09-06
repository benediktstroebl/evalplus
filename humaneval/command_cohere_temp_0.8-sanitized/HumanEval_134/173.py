def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string to words and chech last char is not part of a word
    # If string is empty, return False
    if not txt:
        return False
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_char_is_letter = txt[-1] in letters
    return not last_char_is_letter and txt.split() != ['']