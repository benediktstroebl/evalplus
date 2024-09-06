

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    low = string.lower()
    up = string.upper()

    res = low[::-1] + up[1::]
    return res

