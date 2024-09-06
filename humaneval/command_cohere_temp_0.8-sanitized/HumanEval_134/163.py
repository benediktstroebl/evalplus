def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not belonging to a word, False otherwise.
    """
    # Define and compile regex pattern
    word_pattern = r'\b[a-z]\b'  # using regex to check if the last char is a letter
    
    # Check if the last character is a part of a word
    if re.search(word_pattern, txt) != None:
        return False
    
    # Check if the string is empty
    if txt == "":
        return False
    
    return True