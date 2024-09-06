def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Define and initialize the flag
    is_last_char_not_word_part = False
    
    # Trim any extra space characters at the end of the string (if applicable)
    txt = txt.strip()
    
    # Initialize alphabetical character check
    is_last_char_alpha = txt and txt[-1].isalpha()
    
    # If the last character is alphabetical, check if it's part of a word
    if is_last_char_alpha:
        is_last_char_not_word_part = True
        for word in txt.split(' '):
            if word and word[-1] == txt[-1]:
                is_last_char_not_word_part = False
                break
    
    return is_last_char_not_char_word_part