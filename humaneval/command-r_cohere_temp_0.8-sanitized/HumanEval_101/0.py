def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.

    Args:
        s (str): String of words separated by commas or spaces.

    Returns:
        list: Words as a list of strings.
    """
    return s.split()[::2] + s.split(',')[1::2]