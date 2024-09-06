def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be checked.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extracting the last character and checking if it belongs to the alphabet
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if txt and txt[-1] in alpha:
        # Checking if the last character is not part of a word
        tokens = txt.split()
        if len(tokens) > 0 and tokens[-1] == txt[-1]:
            return True
    return False