def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1]

    # Check if the last character is a letter
    if not last_char.isalpha():
        return False

    # Split the string into words using space as delimiter
    words = txt.split()
    # Reduce the list of words to only the last word
    last_word = words[-1]
    # Check if the last character is the first character of the last word
    if last_char == last_word[0]:
        return False
    return True