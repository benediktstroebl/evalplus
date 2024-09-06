

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lowercase = []
    uppercase = []
    for c in string:
        if c.islower():
            lowercase.append(c)
        elif c.isupper():
            uppercase.append(c)
    return ''.join(lowercase + uppercase)

