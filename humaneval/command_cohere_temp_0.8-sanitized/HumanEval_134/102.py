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
    if len(words) == 0:
        # If an empty string is provided, return False as there are no characters nor words.
        return False
    elif len(words) == 1:
        # If there is only one word, check if the last character is a letter and is not part of a word.
        return txt[-1].isalpha() and txt[-1] not in words[0]
    else:
        # If multiple words are present, ensure the last character is not part of the last word.
        return txt[-1] not in words[-1]