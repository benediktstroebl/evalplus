

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Another way to do this is to use.translate() method
    # https://docs.python.org/3.6/library/stdtypes.html#str.translate
    return string.swapcase()
