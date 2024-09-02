

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    to_upper = ''.join([char.upper() if char.islower() else char.lower() for char in string])
    return to_upper[::-1]

