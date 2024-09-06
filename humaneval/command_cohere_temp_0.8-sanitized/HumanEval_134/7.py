def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Define the last character variable
    last_char = txt[str_len]
    # Check if the string is empty
    if str_len == -1:
        return False
    # Split the string into words using space as a delimiter
    words = txt.split()
    # Reduce the index used to iterate by 1 as the last character has already been added to the words list
    for i in range(str_len, -1, -1):
        if last_char == words[i]:
            return False
    # If the conditions are not met return False
    return True