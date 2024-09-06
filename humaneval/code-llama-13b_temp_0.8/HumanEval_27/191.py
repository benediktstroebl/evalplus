

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip = lambda char: char.swapcase() if char.isalpha() else char
    return ''.join(flip(char) for char in string)

