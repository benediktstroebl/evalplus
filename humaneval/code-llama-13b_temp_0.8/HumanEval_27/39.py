

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Hint: Use str.islower() and str.isupper() to check the case of a character
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
    # return ''.join(map(lambda x: x.lower() if x.isupper() else x.upper(), string))

