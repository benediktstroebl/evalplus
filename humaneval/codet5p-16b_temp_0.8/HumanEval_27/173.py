

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = ''
    for character in string:
        if character.islower():
            flipped += character.upper()
        elif character.isupper():
            flipped += character.lower()
        else:
            flipped += character

    return flipped

