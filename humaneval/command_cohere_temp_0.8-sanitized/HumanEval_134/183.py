def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to retrieve the last character
    len_txt = len(txt)
    
    # Check if the string is empty
    if len_txt == 0:
        return False
    
    # Check if the last character is a letter and not in a word
    last_char = txt[-1]
    is_letter = str.isalpha(last_char)
    is_part_of_word = True  # this is an assumption, as it should be checked afterwards
    if is_letter:
        # Check if the last character is not part of a word
        curr_char_idx = len_txt - 1
        while curr_char_idx > 0 and txt[curr_char_idx - 1] != ' ':
            if not str.isalpha(txt[curr_char_idx - 1]):
                break
            curr_char_idx -= 1
        else:
            is_part_of_word = False

    return is_letter and not is_part_of_word