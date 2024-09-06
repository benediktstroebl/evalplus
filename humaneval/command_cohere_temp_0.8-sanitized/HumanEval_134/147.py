def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to examine.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extract the last character and remove whitespace characters if present
    last_char = txt.strip()[-1:]
    
    # Check if the last character is in a separate word
    # by checking if it is preceded by a space or the beginning of the string
    not_part_of_word = (txt[-1:] != '') or (txt[-1:] == last_char)
    
    # Return True if the last character is alphabetical
    # and not part of a word
    return (last_char.isalpha() and not_part_of_word)