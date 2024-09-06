def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string to be split into words and indexed
    str_tmp = txt.strip()
    
    # Check if the string is empty or has only whitespace characters
    if not str_tmp:
        return False
    
    # Check if the last character is a letter and not the last character of a word
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if str_tmp[-1] in letters and not txt.rsplit(' ', str_tmp.index(str_tmp[-1])).endswith(str_tmp):
        return True
    return False