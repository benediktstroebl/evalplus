def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to examine

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise
    """
    # Use regex to check if the last character is a letter and it is the last character in the string
    alpha_char = r'[a-zA-Z]'
    last_char_is_alone = f'{alpha_char}$'
    
    return bool(re.search(last_char_char, txt) and not re.search(r'\b{}\b'.format(alpha_char), txt))