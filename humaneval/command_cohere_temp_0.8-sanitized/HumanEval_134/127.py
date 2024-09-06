def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

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

    def is_alphabetical(char):
        return char.isalpha()

    def is_not_part_of_word(char):
        return char != ' '

    if not txt:
        return False

    if not txt[-1].strip():
        return False

    last_char = txt[-1]

    if is_alphabetical(last_char) and is_not_part_of_word(last_char):
        return True

    return False