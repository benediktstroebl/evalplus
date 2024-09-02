

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    res = ''
    for char in string:
        if char.islower():
            res += char.upper()
        else:
            res += char.lower()
    return res
