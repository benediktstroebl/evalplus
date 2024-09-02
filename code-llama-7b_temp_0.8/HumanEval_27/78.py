

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    if not isinstance(string, str):
        raise TypeError(f'string must be a string, got {string}')

    flipped_string = ''
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        else:
            flipped_string += char.upper()
    return flipped_string

