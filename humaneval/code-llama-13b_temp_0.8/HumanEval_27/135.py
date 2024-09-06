

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if string == '':
        return ''
    if string.isupper():
        return string.lower()
    if string.islower():
        return string.upper()
    return flip_case(string[1:]) + string[0]
