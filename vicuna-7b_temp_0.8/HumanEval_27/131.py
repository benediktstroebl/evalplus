

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper_case = set(string.upper())
    lower_case = set(string.lower())
    return ''.join(upper_case - lower_case) + ''.join(lower_case - upper_case)
