def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.

    Examples:
    >>> check_if_last_char_is_a_letter("apple pie")
    False
    >>> check_if_last_char_is_a_letter("apple pi e")
    True
    >>> check_if_last_char_is_a_letter("apple pi e ")
    False
    >>> check_if_last_char_is_a_letter("")
    False
    """

    def is_last_char_not_part_of_word(txt):
        # Check if the last character is not whitespace
        if len(txt) == 0:
            return False

        last_char = txt[-1]
        # Check if the last character is a letter
        if not isinstance(last_char, str) or last_char.isalpha() is False:
            return False

        # Check if the last character is the last character of a word
        if txt.rsplit(last_char, 1).count() == 1:
            return True

        return False

    # Remove trailing spaces
    if isinstance(txt, str):
        txt = txt.strip()

    # Call the recursive helper function
    return is_last_char_not_part_of_word(txt)