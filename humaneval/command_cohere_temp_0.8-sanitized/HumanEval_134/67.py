def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be checked.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words
    words = txt.split()
    # Check if the string is empty
    if not words:
        return False
    # Get the last character
    last_char = words[-1][-1]
    # Check if the last character is a letter and is not part of a word
    return ((last_char.isalpha()) and (last_char not in WORDS[0]))
WORDS = ["apple", "pie", "applepi", "e", " "]