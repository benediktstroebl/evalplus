

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(
        [s.upper() if i % 2 == 0 else s.lower() for i, s in enumerate(string)])

