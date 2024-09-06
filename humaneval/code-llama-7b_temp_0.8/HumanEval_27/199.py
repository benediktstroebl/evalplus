

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper_str = string.upper()
    lower_str = string.lower()
    result = ""
    for i, e in enumerate(string):
        if e in upper_str:
            result += lower_str[i]
        elif e in lower_str:
            result += upper_str[i]
        else:
            result += e
    return result

