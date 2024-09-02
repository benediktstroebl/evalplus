

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    new_str = ''
    for c in string:
        if c.islower():
            new_str += c.upper()
        elif c.isupper():
            new_str += c.lower()
        else:
            new_str += c

    return new_str
