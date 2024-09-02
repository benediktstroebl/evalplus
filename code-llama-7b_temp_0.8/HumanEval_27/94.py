

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if string == '':
        return ''
    if string[0].islower():
        return string[0].upper() + string[1:].lower()
    else:
        return string[0].lower() + string[1:].upper()


