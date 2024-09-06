

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = "" # type: str
    for l in string:
        if l.isupper():
            new_string += l.lower()
        elif l.islower():
            new_string += l.upper()
        else:
            new_string += l
            
    return new_string

