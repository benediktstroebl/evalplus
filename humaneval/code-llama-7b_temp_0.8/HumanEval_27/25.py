

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ''
    for char in string:
        new_char = char.swapcase() if char.isalpha() else char
        new_string += new_char
    return new_string

