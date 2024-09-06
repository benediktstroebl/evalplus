def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to examine

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise
    """
    # Use slicing to extract the last character and check if it is an alphabetical character
    last_char = txt[-1:]
    is_alphabetical = last_char.isalpha()

    # Check if the last character is not part of a word by splitting the string and checking if the last element is not an empty string
    words = txt.split()
    is_last_char_not_part_of_word = True if len(words) > 0 and words[-1] != "" else False

    return is_alphabetical and is_last_char_not_part_of_word