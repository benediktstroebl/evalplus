

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([(x.isupper() and x.lower()) or (x.istitle() and x.lower()) or x for x in list(string)])

