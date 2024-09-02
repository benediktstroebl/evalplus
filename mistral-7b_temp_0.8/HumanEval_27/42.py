

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Your code here
    s = ''
    for c in string:
        if c.isupper():
            s += c.lower()
        else:
            s += c.upper()
    return s

