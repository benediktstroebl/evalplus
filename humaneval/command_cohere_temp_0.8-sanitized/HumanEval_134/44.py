def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extracting the last character and removing whitespace
    last_char = txt.strip()[-1:]
    
    # Checking if the last character is a letter and not part of a word
    return (last_char.isalpha() and 
            last_char not in txt.split())