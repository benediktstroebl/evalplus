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
    if (len(words) > 0 and 
            words[-1][-1].isalpha() and 
            not words[-1][-1].isalnum()):
        return True
    # If the last character is part of a word, return False
    elif (len(words) > 0 and 
            words[-1][-1].isalnum()):
        return False
    # If the string ends with a letter that is not part of a word and does not end with a space, True
    elif (txt[-1].isalpha() and 
            not txt[-1].isalnum() and 
            not ends_with_space):
        return True
    # If none of the above matches, return False
    else:
        return False