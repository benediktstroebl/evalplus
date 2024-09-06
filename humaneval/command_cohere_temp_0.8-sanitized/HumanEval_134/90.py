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
    last_char = words[-1][-1] # Using indexing to get the last character of the last element (word) in the list
    # Checking if the last character is alphabetical
    is_alphabetical = str.isalpha(last_Char)
    # Checking if the last character is not part of a word
    is_part_of_word = False
    for word in words:
        if last_char == word[-1]:
            is_part_of_word = True
    return is_alphabetical and not is_part_of_word