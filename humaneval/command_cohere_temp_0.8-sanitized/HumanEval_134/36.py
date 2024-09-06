def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string"

    # Define the word boundary regex pattern
    word_bound = r'\s'

    # Check if the string ends with a space
    if txt.endswith(' '):
        return False

    # Use regex to check if the last character is included in a word
    patch = re.search(r'(?:^|\s)[a-zA-Z]\b(?![a-zA-Z])', txt)

    return bool(patch)