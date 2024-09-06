

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for ch in string:
        if ch.isupper():
            result += ch.lower()
        else:
            result += ch.upper()
    return result

