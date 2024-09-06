

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for s in string:
        if s.isupper():
            result += s.lower()
        else:
            result += s.upper()
    return result
