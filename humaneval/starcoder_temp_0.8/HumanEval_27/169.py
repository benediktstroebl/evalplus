

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # hint: You can change a character to uppercase with.upper() and to lowercase with.lower()
    return string.swapcase()
