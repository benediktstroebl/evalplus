

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    fin_string = ''.join(ch.swapcase() if ch.isupper() else ch.swapcase() for ch in string)
    return fin_string
