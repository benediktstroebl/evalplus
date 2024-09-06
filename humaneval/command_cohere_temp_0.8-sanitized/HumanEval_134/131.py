def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any trailing whitespace from the input string
    txt = txt.rstrip()
    # Check if the last character is a letter and it is not part of a word
    return txt and txt[-1].isalpha() and not txt.split()[-1]
    # Note: The last condition (txt.split()[-1] checks if the last character is not part of a word by verifying if it is not the last segment in a split by space version of the string