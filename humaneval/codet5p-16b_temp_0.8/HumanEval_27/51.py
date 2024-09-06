

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped_string = []
    for char in string:
        if char.isupper():
            flipped_string.append(char.lower())
        else:
            flipped_string.append(char.upper())

    return ''.join(flipped_string)
