

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    new_string = ''
    for ch in string:
        if ch.isupper():
            new_string += ch.lower()
        else:
            new_string += ch.upper()

    return new_string
    

