def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string to be split into words and trailing character
    split_string = txt.rstrip(' ').strip()
    # Check if the string is empty or contains a single space
    if len(split_string) < 2:
        return False
    # Check if the last character is a letter
    if split_string[-1].isalpha():
        # Check if the last character is part of a word
        if split_string.split(' ')[-1] == split_string:
            return False
        else:
            return True
    else:
        return False