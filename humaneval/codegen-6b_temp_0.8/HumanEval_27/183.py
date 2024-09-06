

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    tmp = []
    for c in string:
        if c.isupper() == True:
            tmp.append(c.lower())
        elif c.islower() == True:
            tmp.append(c.upper())
        else:
            tmp.append(c)
    return "".join(tmp)

