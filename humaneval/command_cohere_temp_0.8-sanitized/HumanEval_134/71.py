def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and parse the argument
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Define the word boundary regex
    word_bound = r'\b'

    # Check if the string is empty
    if not txt:
        return False

    # Remove punctuation and split the string into words
    txt = re.sub(r'[^\w\s]', '', txt)
    words = txt.split()

    # If there are no words in the string, the last character is checked against the empty string
    if not words:
        return True if txt[-1].isalpha() else False

    # Otherwise, the last character is checked against the last word
    return True if (words[-1] + '').endswith(txt[-1]) and txt[-1].isalpha() else False