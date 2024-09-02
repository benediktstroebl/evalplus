

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result

