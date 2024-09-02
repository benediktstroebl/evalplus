

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return string.lower().translate(str.maketrans(lower_case, upper_
