

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return ''.join(
        ch.swapcase() if ch.isupper() else ch for ch in string
    )

