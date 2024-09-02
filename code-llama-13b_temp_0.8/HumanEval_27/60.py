

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    out = ''
    for s in string:
        if s.isupper():
            out += s.lower()
        else:
            out += s.upper()
    return out

