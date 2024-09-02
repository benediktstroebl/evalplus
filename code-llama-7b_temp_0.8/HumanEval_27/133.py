

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # return ''.join([(c.upper() if c.islower() else c.lower()) for c in string])

    new_string = ''
    for c in string:
        if c.islower():
            new_string += c.upper()
        else:
            new_string += c.lower()

    return new_string

