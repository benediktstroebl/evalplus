def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to retrieve the last character
    last_char = txt[-1]
    # Check if the last character is a letter and it is not an acronym/part of a word
    is_last_char_not_in_word = (len(txt) >= 2 and txt[-2] != ' ')
    return (last_char.isalpha() and is_last_char_not_in_word)