

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = ''
    for character in string:
        if character.isupper():
            flipped += character.lower()
        elif character.islower():
            flipped += character.upper()
    return flipped

