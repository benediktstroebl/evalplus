

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lowercase = string.lower()
    uppercase = string.upper()
    return lowercase.swapcase()

