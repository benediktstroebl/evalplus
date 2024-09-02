

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([string[i].lower() if string[i].isupper() else string[i].upper() for i in range(len(string))])

