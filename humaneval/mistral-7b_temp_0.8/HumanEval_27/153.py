

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ""
    for i in range(len(string)):
        if string[i].islower():
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string
