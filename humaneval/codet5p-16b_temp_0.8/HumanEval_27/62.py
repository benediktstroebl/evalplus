

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = ""
    for ch in string:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
    return result

