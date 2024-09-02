

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for ch in string:
        if ch.isupper():
            ch = ch.lower()
        elif ch.islower():
            ch = ch.upper()
        result += ch
    return result

