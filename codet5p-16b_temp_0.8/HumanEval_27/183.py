

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    flipped = []
    for char in string:
        if char in upper:
            flipped.append(char.lower())
        elif char in lower:
            flipped.append(char.upper())
        else:
            flipped.append(char)
    return ''.join(flipped)

