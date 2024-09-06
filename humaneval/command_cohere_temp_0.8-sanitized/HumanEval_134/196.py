def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define a regular expression pattern to match alphabetical characters
    pattern = r'[a-zA-Z]'
    # Check if the string is empty
    if not txt:
        return False
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # Check if the last character is part of a word or not
    return pattern not in words[-1]