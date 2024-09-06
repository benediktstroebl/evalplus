

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    s = string.lower()
    out = ""
    for i in s:
        if i.isupper():
            out += i.lower()
        else:
            out += i.upper()
    return out

