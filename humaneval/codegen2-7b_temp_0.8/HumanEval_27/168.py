

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper_characters = []
    lower_characters = []
    for character in string:
        if character.isupper():
            upper_characters.append(character)
        else:
            lower_characters.append(character)
    return ''.join(lower_
