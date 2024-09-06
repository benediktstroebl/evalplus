def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # Check if the string ends with a space
    ends_with_space = txt.endswith(" ")
    # If the string is empty or contains only spaces, return False
    if not txt or txt.replace(" ", "") == "":
        return False
    # If the string ends with a letter that is not part of a word, return True
    if (len(words) > 0 and words[-1][-1].isalpha()) and (not ends_with_space and not words[-1][-1].isdigit()):
        return True
    # Otherwise, return False
    else:
        return False