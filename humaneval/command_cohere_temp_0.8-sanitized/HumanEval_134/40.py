def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extract the last character and check if it's alphabetical
    last_char = txt.strip()[-1]
    if not last_char.isalpha():
        return False

    # Check if the last character is part of a word or not
    words = txt.split()
    if last_char in words[-1]:
        return False
    return True