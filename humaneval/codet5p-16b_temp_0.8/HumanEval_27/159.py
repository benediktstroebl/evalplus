

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    output = []
    for c in string:
        if c.isupper():
            output.append(c.lower())
        else:
            output.append(c.upper())
    return ''.join(output)
