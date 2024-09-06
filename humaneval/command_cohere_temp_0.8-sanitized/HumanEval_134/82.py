def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Check if the string length is smaller than zero and return False if so,
    # meaning that the string ends with a space without any alphabetical character
    # or it is an empty string
    if str_len < 0:
        return False
    # Check if the last character is a letter and it is not the last character of a word,
    # meaning that it is followed by a space or the end of the string
    elif txt[str_len].isalpha() and not txt[str_len].iswalnum():
        return True
    # If the condition is not fulfilled return False
    else:
        return False