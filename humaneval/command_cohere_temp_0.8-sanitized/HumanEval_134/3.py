def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Check if the string is empty
    if not txt:
        return False

    # Remove trailing spaces, if any
    while txt and txt.endswith(" "):
        txt = txt.strip()

    # Check if the last character is alphabetical and not part of a word
    return txt and txt[-1].lower() not in set(" \t\n\r\f,:;'\"!?<>{}[]|=/)")