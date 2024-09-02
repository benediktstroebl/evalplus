

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    ret_str = ''
    for char in string:
        if char.isupper():
            ret_str += char.lower()
        else:
            ret_str += char.upper()
    return ret_str

