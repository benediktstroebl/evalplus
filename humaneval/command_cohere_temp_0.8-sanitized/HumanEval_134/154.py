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

    def is_last_char_not_part_of_word(txt):
        # Check if the last character is whitespace
        if txt[-1] == " ":
            return True

        # Check if the last character is an alphabetical character and not part of a word
        prev_char = None
        curr_char = txt[-1]
        while prev_char != " " and prev_char != None:
            prev_char = txt[txt.rfind(curr_char) - 1]
            if prev_char == " ":
                break
            curr_char = prev_char

        return curr_char.isalpha() and curr_char != " "

    return is_last_char_not_part_word(txt)