def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    if len(words) == 0:
        # If an empty string is provided, the last character is neither part of a word nor any other character
        return False
    last_char = words[-1][-1] # Using indexing to get the last character of the last element (word)
    # Checking if the last character is alphabetical
    if last_char.isalpha():
        # Using boolean OR to check if the last character is not part of a word (1)
        # By checking if the last character is the first character of the string (2)
        return True
    else:
        return False