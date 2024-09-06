

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = []
    for character in string:
        if character.islower():
            flipped.append(character.upper())
        else:
            flipped.append(character.lower())
    return "".join(flipped)

