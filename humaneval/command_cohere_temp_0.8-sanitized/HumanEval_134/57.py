def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to check.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # If the string is empty or has only whitespace characters and no alphanumeric characters, return False
    if not words or all(char.isalnum() for char in words) is False:
        return False
    # Otherwise, get the last character and check if it's a letter and not the last character of a word
    return (len(words) > 0 and words[-1][-1].isalpha() and words[-1][-1] not in ' '.join(words))