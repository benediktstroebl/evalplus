

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip = ""
    for x in string:
        if x.islower():
            flip += x.upper()
        elif x.isupper():
            flip += x.lower()
        else:
            flip += x
    return flip
