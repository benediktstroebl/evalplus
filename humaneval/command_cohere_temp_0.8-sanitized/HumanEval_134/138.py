def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    txt = txt.strip()  # Remove leading/trailing spaces
    last_char = txt[-1]  # Get the last character

    # Check if the last character is a letter and not part of a word
    return (last_char.isalpha() and 
            not txt.split()[-1].startswithOwrds())