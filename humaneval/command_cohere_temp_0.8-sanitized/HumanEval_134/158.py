def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.

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
        # Check if the last character is spaces, digits, or symbols
        if txt[-1].isalpha():
            return True
        # Check if the last character is end of word
        elif txt[-2:] != " ":
            return False
        return True

    # Check if the string is empty
    if not txt:
        return False

    # Remove trailing spaces
    while txt and txt.endswith(" "):
        txt = txt[:-1]

    # If the string is not empty and last character is not part of word, return True
    return is_last_char_not_part_word(txt)