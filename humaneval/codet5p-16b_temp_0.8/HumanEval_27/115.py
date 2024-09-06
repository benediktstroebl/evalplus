

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return "".join([chr(ord(c) ^ ord('a') ^ ord('A')) if c in string.lower() else c for c in string])
