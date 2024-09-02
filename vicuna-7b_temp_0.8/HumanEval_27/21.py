

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([unichr(ord(c) ^ 0x20) if ord(c) < 0x20 else c for c in string])
