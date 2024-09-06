def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input is a string
    if not isinstance(txt, str):
        raise TypeError("The input must be a string")

    # Check if the string is empty
    if not txt:
        return False

    # Remove any whitespace at the end of the string (if present)
    txt = txt.strip()

    # Check if the last character is a letter and not part of a word
    # Note: The split() method returns a list of words (tokens) in the string,
    # and the index -1 refers to the last element (the last character of the string)
    if txt.split()[-1].isalpha() and txt.split()[-1] not in txt.split():
        return True

    return False