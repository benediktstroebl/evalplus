def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define a regular expression pattern to match alphabetical characters
    alpha_pattern = r'[a-zA-Z]'

    # Check if the string is empty
    if not txt:
        return False

    # Find the last character in the string
    last_char = txt[-1]

    # Check if the last character is alphabetic
    if re.search(alpha_pattern, last_char):
        # Check if the last character is separated from the previous word
        return not last_char.isalnum() and re.search(r' \Z', txt)
    return False