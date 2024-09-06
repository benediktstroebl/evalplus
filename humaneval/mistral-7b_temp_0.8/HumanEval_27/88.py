

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    res = ""
    for c in string:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()

    return res

