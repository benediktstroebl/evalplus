

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if string == "":
        return ""
    else:
        if string[0].isupper():
            return string[0].lower() + flip_case(string[1:])
        else:
            return string[0].upper() + flip_case(string[1:])


