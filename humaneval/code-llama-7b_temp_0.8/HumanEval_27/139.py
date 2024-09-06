

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''

    for c in string:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
    return result

