

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    converted_string = ''
    for character in string:
        if character.isupper():
            converted_string += character.lower()
        else:
            converted_string += character.upper()
    return converted_string

