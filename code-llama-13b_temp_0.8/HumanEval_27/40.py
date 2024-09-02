

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = ""
    for i in string:
        if i.islower():
            flipped += i.upper()
        else:
            flipped += i.lower()

    return flipped

