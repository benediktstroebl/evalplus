

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.lower() if string.lower() != string else string
    string = string.upper() if string.upper() != string else string
    return string
