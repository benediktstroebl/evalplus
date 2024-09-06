

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper_letters = string.upper()
    lower_letters = string.lower()
    result = upper_letters + lower_letters
    return result
