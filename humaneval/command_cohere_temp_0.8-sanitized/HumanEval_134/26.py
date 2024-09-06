def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and assign the regex pattern
    word_pattern = r'\w+'
    # Check if the string is empty
    if not txt:
        return False
    while txt[-1] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if txt[-1] not in word_pattern:
            return False
        txt = txt[:-1]
    return True