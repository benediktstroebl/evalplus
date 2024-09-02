

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([ chr(ord("".join(sorted(string.upper()))[0]) - 32 + i) for i in range(len(string)) ])
