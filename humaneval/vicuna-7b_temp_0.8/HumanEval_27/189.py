

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([chr(ord("a") - 1) if ord(c) < ord("a") else chr(ord(c) + 25) for c in string])
