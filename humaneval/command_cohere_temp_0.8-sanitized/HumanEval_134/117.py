def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and assign the variable for the last character in the string
    last_char = txt.strip()[-1]

    # Use a conditional statement to test if the last character is in the string alphabetical order and not in a word
    return (last_char.isalpha() and not last_char.isspace()) or (not last_char.isalpha() and last_char.isspace())