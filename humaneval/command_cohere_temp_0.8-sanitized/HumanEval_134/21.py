def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not part of a word, False otherwise.
    """
    # Define and check if the last character exists and is alphabetic
    last_char = txt[-1:]
    if last_char.isalpha():
        # Check if the last character is a part of a word
        if last_char.lower() in txt.lower():
            return False
        else:
            return True
    else:
        return False