def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Define and check the last character
    last_char = txt[-1:]
    assert isinstance(last_char, str), "Last character must be a string."
    assert last_char.isalpha(), "Last character must be an alphabetical character."

    # Split the string into words
    words = txt.split()
    assert isinstance(words, list), "The split string must be a list."

    # Check if the last character is not part of a word
    if last_char not in words[-1]:
        return True
    else:
        return False