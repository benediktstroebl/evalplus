

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = ""
    for c in string:
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
        result += c
    return result
