def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and compile regex pattern
    word_pattern = r'\b[a-z]\b'  # using regex to match a whole word consisting of a single alphabetical character only
    
    # Use regex to check if the last character is not part of a word
    return not bool(re.search(word_pattern, txt))