

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ''
    for character in string:
        if character.isupper():
            new_character = character.lower()
        else:
            new_character = character.upper()

        new_string += new_character
    return new_string
