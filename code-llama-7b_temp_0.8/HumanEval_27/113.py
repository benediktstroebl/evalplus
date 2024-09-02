

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if len(string) == 1:
        return string.swapcase()

    new_string = ''

    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()

    return new_string

