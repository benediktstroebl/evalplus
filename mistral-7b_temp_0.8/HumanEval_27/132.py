

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    output = ""

    for ch in string:
        if ch.isupper():
            output += ch.lower()
        else:
            output += ch.upper()

    return output

