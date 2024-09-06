def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."

    # Define the word
    word = " ".join(txt.split(" ")[-2:])

    # Check if the last character is a letter and not part of a word
    return (
        len(txt) > 0
        and len(txt) - 1 >= 0
        and txt[-1] in string.ascii_lowercase
        and txt[-1] not in word
    )