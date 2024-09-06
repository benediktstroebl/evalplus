

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return "".join(
        map(
            lambda char: char.lower() if char.isupper() else char.upper(),
            string
        )
    )
    
