

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = ''
    for c in string:
        if c.islower():
            flipped += c.upper()
        else:
            flipped += c.lower()
    return flipped

