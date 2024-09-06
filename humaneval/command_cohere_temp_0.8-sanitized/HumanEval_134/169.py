def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()

    # Check if the string ends with a space followed by a letter
    if txt.endswith(' ') and txt[-1:] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    
    # Check if the last character is a letter that is not part of a word
    # By splitting the string into words and checking if the last character is not part of any word
    if txt.split(' ')[-1][-1].isalpha():
        return True
    
    return False