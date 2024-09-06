def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()
    # Check if the string ends with a space to mitigate the case of a standalone space
    if txt.endswith(' '): 
        return False
    
    # Check if the last character is a letter and not a part of a word
    return (len(txt)>0 and txt[-1] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') and \
           (txt[-1] != '-') and (txt[-1]!='_') and (txt[-1]!='')