def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words based on spaces
    words = txt.split()
    if len(words) == 0:
        # If an empty string is provided, return False as there is no last character.
        return False
    last_char = words[-1][-1] # Using indexing to get the last character

    # Check if the last character is in lowercase or uppercase alphabet
    if last_char in string.ascii_lowercase or last_char in string.ascii_uppercase:
        # Check if the last character is part of a word or punctuation
        if punctuation_last_char_is_part_of_word(words):
            return False
        return True
    return False
def punctuation_last_char_is_part_of_word(words):
    """
    Check if the last character is a punctuation mark and it is part of a word.

    Parameters:
        words (list): List of words split from the input string.

    Returns:
        bool: True if the last character is a punctuation mark and it is part of a word. 
    """
    # Get the last word and last character
    last_word = words[-1]
    last_char = last_word[-1]

    # Check if the last character is a punctuation mark and not appended to a word
    # by checking if the last character is surrounded by alphanumeric characters
    if (last_char in string.punctuation and 
        (last_word[0] in string.ascii_letters or last_word[0] in string.digits) and
        (last_word[-2] in string.ascii_letters or last_word[-2] in string.digits)):
        return True
    return False