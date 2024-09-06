

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = []
    for s in string:
        flipped.append(s.lower() if s.isupper() else s.upper())
    return "".join(flipped)
