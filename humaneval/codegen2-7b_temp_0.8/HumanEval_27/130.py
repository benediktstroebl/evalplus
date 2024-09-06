

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    return ''.join([x if x.islower() else chr(ord(x) ^ 0x20) for x in string])
