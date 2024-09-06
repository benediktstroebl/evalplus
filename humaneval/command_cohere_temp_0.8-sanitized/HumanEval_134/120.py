def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and check if the last character exists and it's alphabetic
    last_char = txt[-1:]
    if last_char.isalpha() == False or len(last_char) != 1:
        return False

    # Check if the last character is not part of a word
    words = txt.split()
    if last_char in ' '.join(words):
        return False

    return True