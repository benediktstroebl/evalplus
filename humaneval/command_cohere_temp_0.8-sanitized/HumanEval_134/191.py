def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input must be a string"
    # Split the text on spaces to words
    words = txt.split()
    # Remove trailing spaces and extract the last character
    last_char = txt.strip()[-1:]
    # Check if the last character is a letter and not part of a word
    return (last_char.isalpha() and 
            last_char not in ['', words[-1][-1:] ])