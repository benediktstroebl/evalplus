

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lowercase_chars = string.lower()
    uppercase_chars = string.upper()
    return lowercase_chars + uppercase_chars[::-1]

