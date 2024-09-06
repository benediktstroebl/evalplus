

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for i in range(len(string)):
        if string[i].islower():
            result += string[i].upper()
        elif string[i].isupper():
            result += string[i].lower()
        else:
            result += string[i]
    return result

