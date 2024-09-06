def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # If the string is empty or there are no words at all, return False
    if not txt or not words:
        return False
    # Reduce the list of words to the last character with space stripping
    last_char = '/'.join(words[-1:]).strip(' ')
    # Return True if the last character is a alphabetical character not part of a word
    return bool(last_char) and last_char.isalpha() and not last_char.isalpha()