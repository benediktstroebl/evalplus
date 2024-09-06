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
    if len(words) == 0:  # If an empty string is provided, return False as it cannot have a last character
        return False
    last_char = words[-1][-1]  # Using indexing to get the last character of the last element (word) in the list

    # Check if the last character is alphabetical and not part of a word
    return (last_char.isalpha() and not bool(re.match(r'[a-zA-Z]\b', last_Char)))