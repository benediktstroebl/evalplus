def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Extract the last character and remove spaces
    last_char = txt.strip().split(' ')[-1][-1]

    # Check if the last character is in alphabetical order and not part of a word
    return (last_char.isalpha() and not bool(re.search(r'\b\w+\b', last_char)))