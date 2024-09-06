

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if isinstance(string, str):
        flipped_string = ''
        for character in string:
            if character.isupper():
                flipped_string += character.lower()
            else:
                flipped_string += character.upper()
        return flipped_string
    else:
        raise TypeError('Input is not a string.')

