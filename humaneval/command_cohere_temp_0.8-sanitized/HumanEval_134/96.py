def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: Indicating whether the last character is an alphabetical character and not part of a word.
    """
    # Remove trailing spaces
    while txt and txt.endswith(" "):
        txt = txt.strip()
    
    # Check if the last character is a letter and not part of a word
    return (txt and (txt[-1].isalpha() and not txt.split()[-1]) )