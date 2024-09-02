

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lowercase_string = string.lower()
    uppercase_string = string.upper()

    return lowercase_string + uppercase_string

