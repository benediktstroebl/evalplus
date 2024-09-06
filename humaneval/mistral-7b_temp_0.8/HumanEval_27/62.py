

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    case = ""
    for i in string:
        if i.isupper():
            case += i.lower()
        else:
            case += i.upper()
    return case

