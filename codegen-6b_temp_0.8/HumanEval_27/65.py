

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.swapcase() if c.isupper() else c.upper() if c.islower() else c for c in string])

