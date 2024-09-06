

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for i in range(0, len(string)):
        if string[i].isupper():
            result += string[i].lower()
        elif string[i].islower():
            result += string[i].upper()
        else:
            result += string[i]
    return result


