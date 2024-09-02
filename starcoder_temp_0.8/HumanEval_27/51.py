

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = ""
    for ch in string:
        if ch.isupper():
            new_str += ch.lower()
        else:
            new_str += ch.upper()
    return new_str
