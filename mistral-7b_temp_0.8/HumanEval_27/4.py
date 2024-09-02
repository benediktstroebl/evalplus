

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_str = string.lower()
    upper_str = string.upper()
    return lower_str.swapcase()

