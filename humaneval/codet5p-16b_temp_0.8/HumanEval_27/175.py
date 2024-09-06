

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    s = ''
    for char in string:
        if char.islower():
            s = s + char.upper()
        else:
            s = s + char.lower()
    return s

