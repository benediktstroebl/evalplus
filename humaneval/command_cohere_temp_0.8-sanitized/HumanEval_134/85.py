def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string to be split into words and cleaned
    txt = txt.split(' ')[-1].strip()
    # Use the regex to check if the last character is a letter and is not part of a word
    # By using the '^' it will only match the character if it is not part of a word,
    # and by using the '\s' it will also ensure that it is not a part of a word with spaces
    return bool(re.match(r"[a-zA-Z]\Z[^\s\w]*", txt))