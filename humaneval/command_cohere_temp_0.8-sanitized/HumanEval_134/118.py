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

    def is_not_word(char):
        # Check if the last character is not part of a word
        return char.startswith(' ') or char.startswith('\t') or char.startswith('-') or char.startswith('_') or char.startswith('\"') or char.startswith("'")

    if not txt.strip():
        return False
    
    last_char = txt.strip().split()[-1]
    
    return is_alphabetical(last_char) and is_not_word(last_Char)