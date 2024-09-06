def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Define the word boundary regex pattern
    word_boundry = r"\s"

    # Check if the string is empty
    if not txt:
        return False

    # Use regex to check if the last character is included in a word
    is_last_char_in_word = bool(re.search(r"[a-zA-Z]\s*", txt))

    return not is_last_char_in_word