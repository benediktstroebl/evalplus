

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = list(string)
    for i in range(len(string)):
        if string[i].isupper():
            new_string[i] = string[i].lower()
        elif string[i].islower():
            new_string[i] = string[i].upper()
    return ''.join(new_string)


