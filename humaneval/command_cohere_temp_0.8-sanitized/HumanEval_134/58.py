def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Remove whitespace characters and convert to lowercase to handle cases sensitively
    txt = txt.strip().lower()
    # Split the string into words using a space as the delimiter
    words = txt.split()
    # Check if the string is empty or the last character is a word delimiter
    if len(txt) == 0 or words[-1][-1] in "&;,.:!?()[]{}\"'<>/-" :
        return False
    # Check if the last character is an alphabetical character and not part of a word
    return words[-1][-1].isalpha() and not words[-1][-1].isalnum()