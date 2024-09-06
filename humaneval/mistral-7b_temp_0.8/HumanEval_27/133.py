

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    res = ""
    for char in string:
        if char.isupper():
            res += char.lower()
        else:
            res += char.upper()
    return res

