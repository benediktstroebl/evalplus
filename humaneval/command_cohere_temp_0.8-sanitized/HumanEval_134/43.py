def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extracting the last character and checking if it's a letter
    last_char = txt[-1:]
    if not isinstance(last_char, str):
        return False
    if not str.isalpha(last_char):
        return False

    # Further checks to ensure the last character is not part of a word
    split_str = txt.split()
    if len(split_str) == 0:
        return False
    if split_str[-1] == last_char:
        return False
    return True