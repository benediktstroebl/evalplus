

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flip = []
    for char in string:
        if char.isalpha():
            flip.append(char.swapcase())
        else:
            flip.append(char)

    return ''.join(flip)

