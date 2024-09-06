def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Check if the string length is smaller than 1 and return False if so
    if str_len < 1:
        return False
    # Extract the last character from the string
    last_char = txt[str_len]
    # Check if the last character is lowercase or uppercase
    if last_char.isalpha():
        # Split the string into words through space
        words = txt.split()
        # Define the last element of the list of words
        last_word = words[-1]
        # Check if the last character is in the last word
        if last_char in last_word:
            return False
        else:
            return True
    else:
        return False