

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join(chr(ord(c) ^ 32) if c.isupper() else chr(ord(c) ^ 32) for c in string)
