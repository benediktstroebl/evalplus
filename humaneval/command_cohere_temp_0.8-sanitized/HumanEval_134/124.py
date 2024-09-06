def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Define the last character variable
    last_char = txt[str_len]
    # Check if the string length is smaller than one
    if str_len < 1:
        return False
    # Check if the last character is a space
    if last_char == " ":
        return False
    # Check if the last character is lowercase or uppercase letter
    if last_char.isalpha():
        # Split the string into words through space
        words = txt.split()
        # Define the variable for the last word index
        last_word_index = len(words) - 1
        # Check if the last character is the last word or not
        if last_char == words[last_word_index]:
            return True
        else:
            return False
    else:
        return False