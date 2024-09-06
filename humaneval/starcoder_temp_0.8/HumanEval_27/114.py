

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    return ''.join(map(lambda s: s.lower() if s.isupper() else s.upper(), string))

