

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([chr(ord("a") - 1) if c.isupper() else chr(ord(c) - 32) if c.islower() else c for c in string])