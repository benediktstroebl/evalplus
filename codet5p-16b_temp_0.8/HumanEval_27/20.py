

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = ""
    for c in string:
        if c.isupper():
            flipped += c.lower()
        else:
            flipped += c.upper()
    return flipped
