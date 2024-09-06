

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper()
    string = string.replace(string.lower(), string.upper())
    string = string.replace(string.upper(), string.lower())
    return string
