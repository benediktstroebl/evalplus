def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string to words and letters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = txt.split()
    if len(words) == 0:
        # If the string contains only spaces
        return False
    elif len(words) == 1:  # Only 1 word
        return words[-1][-1] in letters
    else:
        # More than 1 word
        for i in range(len(words) - 1, -1, -1):
            if words[i][-1] in letters:
                return True
            elif words[i][-1] in ' ':
                continue
            else:
                return False