def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string before checking
    if txt and isinstance(txt, str):
        txt = txt.rstrip()
    # Check if the string ends with a space separated word
    if txt.split(" ")[-1] != '':
        # Check if the last character is a letter
        if txt[-1].isalpha():
            return True
    return False