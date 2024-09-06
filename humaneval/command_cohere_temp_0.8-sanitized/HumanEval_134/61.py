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

    def is_alphabetical(char):
        return char.isalpha()

    def is_last_char(txt):
        return txt[-1] == txt[-2] if len(txt) > 1 else False

    def is_not_part_of_word(txt):
        words = txt.split()
        return len(words) == 0 or (len(words) == 1 and is_alphabetical(txt[-1]))

    return is_last_char(txt) and is_not_part_of_word(txt)