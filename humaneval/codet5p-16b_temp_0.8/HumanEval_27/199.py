

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    string = list(string)
    for i in range(len(string)):
        if string[i].islower():
            string[i] = string[i].upper()
        else:
            string[i] = string[i].lower()
    return ''.join(string)

