def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()
    # Check if the string ends with a space
    if txt.endswith(" "):
        return False
    # Check if the string ends with a letter character
    elif txt[-1].isalpha():
        # Check if the last character is part of a word
        if txt[-1] in txt.split():
            return False
        else:
            return True
    else:
        return False