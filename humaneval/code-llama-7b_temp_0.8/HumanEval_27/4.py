

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ""
    for c in string:
        if c.islower():
            new_string += c.upper()
        elif c.isupper():
            new_string += c.lower()
        else:
            new_string += c
    return new_string

