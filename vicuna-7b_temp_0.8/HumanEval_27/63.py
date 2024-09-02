

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # use a dictionary to map lowercase characters to uppercase and vice versa
    # to efficiently flip the case of characters
    case_map = {ord(c): ord(c.upper()) for c in string}
    return ''.join([case_map[c] if c.isupper() else c for c in string])
