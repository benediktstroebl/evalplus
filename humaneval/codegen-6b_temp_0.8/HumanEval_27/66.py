

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lstring = list(string)
    for i in range(len(string)):
        if lstring[i].isupper():
            lstring[i] = lstring[i].lower()
        elif lstring[i].islower():
            lstring[i] = lstring[i].upper()
    return ''.join(lstring)

