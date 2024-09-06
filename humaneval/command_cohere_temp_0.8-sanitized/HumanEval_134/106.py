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

    # Define the criteria to be met
    letter_not_in_word = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

    # Check if the string is empty
    if not txt:
        return False

    # Remove trailing spaces
    while txt and txt.endswith(' '):
        txt = txt.strip()

    # Check if the last character is a letter and is not a part of a word
    return txt[-1].lower() not in map(str.lower, letter_not_in_word)