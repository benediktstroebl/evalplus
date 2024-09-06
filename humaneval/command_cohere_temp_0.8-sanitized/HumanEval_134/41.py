def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as delimiters
    words = txt.split()
    # If the string is empty or there are no words at all, return False
    if not txt or not words:
        return False
    # Reduce the list of words to only the last character of the string, using the built-in function `pop()`
    last_char = words.pop()
    # If the last character is alphabetical and not part of a word, return True, otherwise return False
    if isinstance(last_char, str) and len(last_char) == 1 and str.isalpha(last_char):
        return True
    return False