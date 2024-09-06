def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string minus the last character
    preface = txt[:-1]
    # Check if the last character is part of a word
    # by checking if it is preceded by a space character.
    return (txt[-1].isalpha() and not preface.rstrip().endswith(txt[-1])) if txt else False