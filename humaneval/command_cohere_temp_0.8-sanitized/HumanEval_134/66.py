def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string"
    
    # Define the word boundary regex pattern
    word_boundry = r'\s'

    # Use regex to check if the last character is part of a word or not
    return not bool(re.search(f'(?<!\W){txt[-1]}{word_boundry}', txt))