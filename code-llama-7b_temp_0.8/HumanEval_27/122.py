

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join(
        [character.lower() if character.isupper() else character.upper() for character in string]
    )

