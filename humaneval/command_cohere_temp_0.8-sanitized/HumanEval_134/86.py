def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not part of a word, False otherwise.
    """
    # Define a list of punctuation that splits words
    punctuations = [' ', '.', ',', ';', '!', '?', '(', ')', '{', '}', '[', ']', '<', '>', '"', "'", '/', '\\']
    # Check if the variable text is not empty
    if not txt:
        return False
    # Split the text into words to check if the last character is not part of a word
    words = txt.split()
    # Check if the last character is a letter and not part of a word
    if len(words) > 0 and words[-1][-1].isalpha():
        for char in words[-1][-1]:
            if char not in punctuations:
                return False
        return True
    return False