

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    res = ""
    for c in string:
        if c.isalpha():
            if c.isupper():
                res += c.lower()
            elif c.islower():
                res += c.upper()
            else:
                res += c
        else:
            res += c
    return res

