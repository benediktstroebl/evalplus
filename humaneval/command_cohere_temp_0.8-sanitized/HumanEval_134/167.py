def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a whitelist of punctuation that is allowed to separate letters from words
    punct = '.!?()-'
    # Split the string into words and check if the last character is a letter and is not part of a word
    return (txt.split(' ')[-1][-1].isalpha() and not txt.split(' ')[-1][-1].lower() in punct)