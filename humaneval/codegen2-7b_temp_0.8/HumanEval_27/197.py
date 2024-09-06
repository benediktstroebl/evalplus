

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([string[i].swapcase() if i in string.lower() else string[i].lower() for i in range(len(string))
