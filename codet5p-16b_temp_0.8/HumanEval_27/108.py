

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = ''
    for ch in string:
        if ch.isupper():
            flipped += ch.lower()
        elif ch.islower():
            flipped += ch.upper()
        else:
            flipped += ch
    return flipped

