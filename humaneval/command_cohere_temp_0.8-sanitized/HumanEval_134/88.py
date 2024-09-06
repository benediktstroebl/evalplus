def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Use slicing to extract the last character and assign it to a variable
    char = txt[-1]
    # Use a dictionary to check if the last character is an alphabetical character
    if char in ALPHABET:
        # Check if the last character is not part of a word by evaluating its whitespace property
        if not txt.rsplit(' ', 1)[-1]:
            return True
    return False
ALPHABET = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}