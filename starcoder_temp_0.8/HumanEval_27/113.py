

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new = ''
    for i in string:
        if i.islower():
            new += i.upper()
        else:
            new += i.lower()
    return new
