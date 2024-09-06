

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([Character.from_ell(ord(char)) if ord(char) < 128 else Character.from_eell(ord(char)) for char in string])
